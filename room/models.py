from django.db import models

from django.contrib.auth.models import User

class Student(models.Model):
     CLASS_CHOICES = [
         ('2019MPFT-Aug5-Sep6','2019MPFT-Aug5-Sep6'),
     ]
     PARTICIPATE_CHOICES=[
         ('Yes','Yes'),
         ('No','NO'),
         ('Maybe','Maybe')
     ]
     CORE_CHOICES=[
         ('Yes','Yes'),
         ('No','NO'),
         ('Maybe','Maybe')
     ]
     INFLUENCE_CHOICES=[
         ('Facebook','Facebook'),
         ('Twitter','Twitter'),
         ('Alumni','Alumni'),
         ('Event','Event'),
         ('Instagram','Instagram'),
         ('Moringa-Website','Moringa-Website'),
         ('Referall','Referall'),
         ('Google','Google'),
         ('Nairobi-Tech-Week','Nairobi-Tech-Week'),
         ('Other','Other')
     ]
     HEAR_CHOICES=[
         ('Facebook','Facebook'),
         ('Twitter','Twitter'),
         ('Alumni','Alumni'),
         ('Event','Event'),
         ('Instagram','Instagram'),
         ('Moringa-Website','Moringa-Website'),
         ('Referall','Referall'),
         ('Google','Google'),
         ('Nairobi-Tech-Week','Nairobi-Tech-Week'),
         ('Other','Other')
     ]
     EDUCATION_CHOICES=[
         ('High-School',''),
         ('Diploma',''),
         ('Bachelor-Degree','Bachelor-Degree'),
         ('Masters','Masters'),
         ('Doctorate','Doctorate'),
         ('Other','Other')

     ]
     GENDER_CHOICES=[
         ('Male','Male'),
         ('Female','Female'),
         ('Prefer not to say','Prefer not to say')
     ]
     PAY_CHOICES=[
         ('Yes','Yes'),
         ('No','No')
     ]
    first_name = models.CharField(max_length =40)
    last_name = models.CharField(max_length =40)
    email = models.CharField(max_length =100)
    class_name = models.CharField(max_length =100)
    phone_no =   models.IntegerField(default=0, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True)
    participation_training = models.CharField(choices=PARTICIPATE_CHOICES, null=True)
    core_join =models.CharField(choices=CORE_CHOICES, null=True)
    hear = models.CharField(choices=HEAR_CHOICES, null=True)
    influence =models.CharField(choices=INFLUENCE_CHOICES, null=True)
    pay = models.CharField(choices=PAY_CHOICES, null=True)
    education =models.CharField(choices=EDUCATION_CHOICES, null=True)
    article_link = models.CharField(max_length =100)
