from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

def new_phone_number():
    # client = Client(account_sid, auth_token)

    # numbers = client.available_phone_numbers("US") \
    #                 .local \
    #                 .list(area_code="510")

    # number = client.incoming_phone_numbers \
    #             .create(phone_number=numbers[0].phone_number)
    return '+16082386456'


def serialize_questions(question_query):
    return [question for question in question_query.values('id', 'question_type', 'content')]