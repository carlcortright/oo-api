from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse

from datetime import datetime

from .models import Classroom, Question
from django.db.utils import IntegrityError
from .utils import new_phone_number, serialize_questions, parse_question_type
import json


def display_classroom(request, name):
    """ Gets all of the data for a class including name, phone number and questions
    """
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
    """ Lists all of the questions associated with a classroom. 
        We poll this endpoint from the frontend to look for new questions.
    """
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
    """ Creates a new classroom in the database
    """
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    name = body['name']
    # Validate the class name
    if ' ' in name:
        return JsonResponse({'error': 'invalid class name'})
    # Try to create a new classroom with a unique phone number
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
    """ Endpoint used by twilio to receive new questions
        We don't hit this endpoint directly. Instead twilio posts to it
        when a new text is received
    """
    resp = MessagingResponse()
    # First find the classroom associated with the phone number texted
    phone_number = request.POST['To']
    try:
        classroom = Classroom.objects.get(phone_number=phone_number)
    except:
        resp.message("Class does not exist")
        return HttpResponse(resp)
    # Create a new question from the text received
    try: 
        question_code, question_text = parse_question_type(request.POST['Body'])
        Question.objects.create(
            content=question_text,
            classroom=classroom,
            created=datetime.now(),
            question_type=question_code
        )
    except:
        resp.message("Server Error")
        return HttpResponse(resp)
    resp.message("Question received!")
    return HttpResponse(resp)