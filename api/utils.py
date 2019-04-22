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