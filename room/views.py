from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
# @login_required(login_url='/accounts/login/')
def add_student(request):

   current_user = request.user

   if request.method == 'POST':
       
       form = StudentForm(request.POST)
       if form.is_valid():
           stude = form.save(commit=False)
           stude.user=current_user
           stude.save()
    
   else:
       form = StudentForm()

   return render(request,'student.html',locals())
=======

# Create your views here.
>>>>>>> origin/feature/emma
=======
from .models import *


>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
