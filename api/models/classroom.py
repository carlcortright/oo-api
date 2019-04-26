from django.db import models
from django.core.validators import RegexValidator

class Classroom(models.Model):
    """ Default classroom model
        Acts as the model datastore for everything in the classroom response
    """
    class_name = models.CharField(max_length=255, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)