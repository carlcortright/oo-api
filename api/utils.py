import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH')

def new_phone_number():
    client = Client(account_sid, auth_token)

    numbers = client.available_phone_numbers("US") \
                    .local \
                    .list()
    number = client.incoming_phone_numbers \
                .create(
                    phone_number=numbers[0].phone_number,
                    sms_url='http://' + os.getenv('WEBHOOK') + '/api/receive_question'
                )
    return number.phone_number


def serialize_questions(question_query):
    return [question for question in question_query.values('id', 'question_type', 'content', 'created')]

def parse_question_type(question_text):
    text = question_text.lower()
    if text[0:2] == 'gn':
        return 'GN', question_text[2:]
    elif text[0:2] == 'tf':
        return 'TF', question_text[2:]
    elif text[0:2] == 'sa':
        return 'SA', question_text[2:]
    elif text[0:2] == 'cm':
        return 'CM', question_text[2:]
    else:
        return 'GN', question_text