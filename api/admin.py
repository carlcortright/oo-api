from django.contrib import admin
from .models import Question, Classroom

# Adds all of the models to the admin so we can administer
admin.site.register(Question)
admin.site.register(Classroom)