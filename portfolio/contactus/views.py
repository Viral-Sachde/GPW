from django.shortcuts import render, redirect

# Create your views here.
# Add the two views we have been talking about  all this time :)

from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from .models import ContactUs
from django.contrib import messages



def HomePage(request):
    return render(request, "index.html")


def savey(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ab = ContactUs(name=name, email=email, subject=subject, message=message)
        ab.save()
        messages.success(request,'Your Message has been sent successfully!!')
    return redirect('home')