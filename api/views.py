from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse



def display_classroom(request):
    mock_data = {
        "phone_number": "(111) 222-3334",
        "class_id": "Principles of OO",
        "questions": [
            {
                "id": 1,
                "type": "t/f",
                "question": "Do we want to use encapsulation in OO programming"
            },
            {
                "id": 0,
                "type": "long answer",
                "question": "when is the semester project due?"
            }
        ]
    }
    return JsonResponse(mock_data)


def list_questions(request):
    mock_data = [
        {
            "id": 1,
            "type": "t/f",
            "question": "Do we want to use encapsulation in OO programming"
        },
        {
            "id": 0,
            "type": "long answer",
            "question": "when is the semester project due?"
        }
    ]
    return JsonResponse(mock_data, safe=False)


def create_classroom(request):
    return JsonResponse({"created": True})

@csrf_exempt
def receive_question(request):
    resp = MessagingResponse()

    # Add a message
    resp.message("Got it" + str(request.POST) + "body: " + str(request.body))

    return HttpResponse(str(resp))