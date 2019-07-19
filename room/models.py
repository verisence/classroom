from django.db import models

<<<<<<< HEAD
<<<<<<< HEAD

# Create your models here.

from django.contrib.auth.models import User

class Student(models.Model):
    CLASS_CHOICES = [
         ('2019MPFT-Aug5-Sep6','2019MPFT-Aug5-Sep6'),
     ]
    PARTICIPATE_CHOICES=[
=======
from django.contrib.auth.models import User

class Student(models.Model):
     CLASS_CHOICES = [
         ('2019MPFT-Aug5-Sep6','2019MPFT-Aug5-Sep6'),
     ]
     PARTICIPATE_CHOICES=[
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
         ('Yes','Yes'),
         ('No','NO'),
         ('Maybe','Maybe')
     ]
<<<<<<< HEAD
    CORE_CHOICES=[
=======
     CORE_CHOICES=[
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
         ('Yes','Yes'),
         ('No','NO'),
         ('Maybe','Maybe')
     ]
<<<<<<< HEAD
    INFLUENCE_CHOICES=[
=======
     INFLUENCE_CHOICES=[
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
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
<<<<<<< HEAD
    HEAR_CHOICES=[
=======
     HEAR_CHOICES=[
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
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
<<<<<<< HEAD
    EDUCATION_CHOICES=[
=======
     EDUCATION_CHOICES=[
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
         ('High-School',''),
         ('Diploma',''),
         ('Bachelor-Degree','Bachelor-Degree'),
         ('Masters','Masters'),
         ('Doctorate','Doctorate'),
         ('Other','Other')

     ]
<<<<<<< HEAD
    GENDER_CHOICES=[
=======
     GENDER_CHOICES=[
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
         ('Male','Male'),
         ('Female','Female'),
         ('Prefer not to say','Prefer not to say')
     ]
<<<<<<< HEAD
    PAY_CHOICES=[
         ('Yes','Yes'),
         ('No','No')
     ]

=======
     PAY_CHOICES=[
         ('Yes','Yes'),
         ('No','No')
     ]
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
    first_name = models.CharField(max_length =40)
    last_name = models.CharField(max_length =40)
    email = models.CharField(max_length =100)
    class_name = models.CharField(max_length =100)
<<<<<<< HEAD
    phone_no =   models.CharField(max_length=50)
    gender = models.CharField(max_length =100, choices=GENDER_CHOICES, null=True)
    participation_training = models.CharField(max_length =100, choices=PARTICIPATE_CHOICES, null=True)
    core_join =models.CharField(max_length =100, choices=CORE_CHOICES, null=True)
    hear = models.CharField(max_length =100, choices=HEAR_CHOICES, null=True)
    influence =models.CharField(max_length =100, choices=INFLUENCE_CHOICES, null=True)
    pay = models.CharField(max_length =100, choices=PAY_CHOICES, null=True)
    education =models.CharField(max_length =100, choices=EDUCATION_CHOICES, null=True)
    article_link = models.CharField(max_length =100)
  
  
    def save_student(self):
        self.save()

    
    
=======
# Create your models here.
>>>>>>> origin/feature/emma
=======
    phone_no =   models.IntegerField(default=0, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True)
    participation_training = models.CharField(choices=PARTICIPATE_CHOICES, null=True)
    core_join =models.CharField(choices=CORE_CHOICES, null=True)
    hear = models.CharField(choices=HEAR_CHOICES, null=True)
    influence =models.CharField(choices=INFLUENCE_CHOICES, null=True)
    pay = models.CharField(choices=PAY_CHOICES, null=True)
    education =models.CharField(choices=EDUCATION_CHOICES, null=True)
    article_link = models.CharField(max_length =100)
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
