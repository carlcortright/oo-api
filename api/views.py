from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse

from .models import Classroom, Question
from django.db.utils import IntegrityError
from .utils import new_phone_number, serialize_questions


def display_classroom(request, name):
    # Get the classroom db object the user is trying to access
    try:
        classroom = Classroom.objects.get(class_name=name)
    except:
        return JsonResponse({'error': 'class not found'})
    # Get all of the questions related to the classroom
    try:
        questions = classroom.question_set.all()
        serialized_questions = serialize_questions(questions)
    except:
        return JsonResponse({'error': 'server error'})
    # Return the class data
    data = {
        "phone_number": classroom.phone_number,
        "class_name": classroom.class_name,
        "questions": serialized_questions
    }
    return JsonResponse(data)


def list_questions(request):
    try:
        classroom = request.GET['classroom']
        latest_question_id = int(request.GET['id'])
    except:
        return JsonResponse({'error': 'invalid params, classroom and id required'})
    # Get the classroom db object the user is trying to access
    try:
        classroom = Classroom.objects.get(class_name=classroom)
    except:
        return JsonResponse({'error': 'class not found'})
    # Get all of the questions related to the classroom after the specified id
    try:
        questions = classroom.question_set.all().filter(id__gt=latest_question_id)
        serialized_questions = serialize_questions(questions)
    except:
        return JsonResponse({'error': 'server error'})
    # Return the question data
    return JsonResponse(serialized_questions, safe=False)


def create_classroom(request):
    name = request.POST['name']
    if ' ' in name:
        return JsonResponse({'error': 'invalid class name'})
    try:
        number = new_phone_number()
        classroom = Classroom.objects.create(
            class_name=name,
            phone_number=number
        )
    except IntegrityError: 
        return JsonResponse({'error': 'class name already exists'})
    return JsonResponse({'class_name': name})


def receive_question(request):
    resp = MessagingResponse()
    phone_number = request.POST['To']
    try:
        classroom = Classroom.objects.get(phone_number=phone_number)
    except:
        resp.message("Class does not exist")
        return HttpResponse(resp)
    try: 
        Question.objects.create(
            content=request.POST['Body'],
            classroom=classroom
        )
    except:
        resp.message("Server Error")
        return HttpResponse(resp)
    resp.message("Question received!")
    return HttpResponse(resp)