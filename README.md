# API for Class Q&A

> API for classqa.carl.fun

*This repository is split into two repositories. Below is the link to our frontend.*
https://github.com/carlcortright/oo-frontend

# Group Members
Carl Cortright and Avery Olson

# Project Overview

In class, many students don’t have the courage to ask a question in front of a large lecture. We plan to develop a webapp that will allow a student who has a question to text a phone number, adding their question to a queue for the professor to answer. The professor can then scan questions, and if the question is going to be answered in the upcoming slides she can then decide to defer answering until it is covered. 

# Installing and executing

First install virtualenv if you dont have it:
`pip3 install virtualenv`

Then create a new virtual environment. Make sure to do this in the project directory. This isolates the package installs you do so it doesn’t mess with your python env:
`virtualenv env`

Next activate and install the project requiremnts:
`source env/bin/activate`
`pip install -r requirements.txt`

Next set up a .env file with local environment variables. Create a file called `.env` in the root of this project with the following content:

```
TWILIO_SID=xxxxx
TWILIO_AUTH=xxxxxx
WEBHOOK=domain.ngrok.io
DEBUG=True
SECRET_KEY=xxxxx
```

Then you can set up the local database:
`python manage.py migrate`

Finally run the dev server:
`python manage.py runserver`

Running with text messages locally requires an ngrok account. 
