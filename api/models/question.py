from django.db import models
from datetime import date
from .classroom import Classroom

class Question(models.Model):
    """ Question model that holds all of the data for a single question
    """

    # This enumerator defines the options for the question ytpes
    QUESTION_TYPE_CHOICES = (
        ('GN', 'GENERAL'),
        ('TF', 'TRUE/FALSE'),
        ('SA', 'SHORT ANSWER'),
        ('CM', 'COMMENT')
    )
    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE_CHOICES,
        default="GN")
    content = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    created = models.DateTimeField(default=date.today)