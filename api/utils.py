import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH')

def new_phone_number():
    """ Provisions a new phone number from twilio. 
        On success, this method returns the phone number created.
    """
    client = Client(account_sid, auth_token)

    numbers = client.available_phone_numbers("US") \
                    .local \
                    .list()
    # Create a new phone number and register it to our recieve question endpoint
    number = client.incoming_phone_numbers \
                .create(
                    phone_number=numbers[0].phone_number,
                    sms_url='http://' + os.getenv('WEBHOOK') + '/api/receive_question'
                )
    return number.phone_number


def serialize_questions(question_query):
    """ Creates a list of questions that are formatted in a dictionary
        Makes returning lists of questions easy
    """
    return [question for question in question_query.values('id', 'question_type', 'content', 'created')]

def parse_question_type(question_text):
    """ Parses the type of the question from the text
    """
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