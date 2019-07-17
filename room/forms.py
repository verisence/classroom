from .models import Student
from django import forms
from django.forms import Modelform, Textarea, IntegerField

class StudentForm(forms.Modelform):
    class Meta:
        model = Student
        exclude = ['user']