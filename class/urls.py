"""class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

from django.conf.urls import url
from django.conf.urls import url,include

=======
from django.conf.urls import url
>>>>>>> origin/feature/emma
=======
from django.conf.urls import url,include
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
=======

from django.conf.urls import url
from django.conf.urls import url,include

>>>>>>> origin/austin
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

     url(r'',include('room.urls')),

=======
>>>>>>> origin/feature/emma
=======
     url(r'',include('room.urls')),
>>>>>>> e7c3181bd584e228b87694c2d0e35db72f51b3cd
=======

     url(r'',include('room.urls')),

>>>>>>> origin/austin
]
