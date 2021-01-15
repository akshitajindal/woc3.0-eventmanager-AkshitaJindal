from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from .models import eventRegistration
from .models import participantRegistration
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget, AdminTimeWidget
#from .forms import event_registration_form

# Create your views here.

def home(request):
    return render(request, 'home.html')

def event_registration(request):
    if request.method == 'GET':
        #form = event_registration_form
        #return render(request, 'event_registration_page.html', {
        #    'form': form,
        #})
        return render(request, 'event_registration_page.html')
        #return HttpResponse("Get method")
    elif request.method == 'POST':
        #form = event_registration_form(request.POST)
        #if form.is_valid():
        #    form.save()
        #    return HttpResponse("Saved")
        event_name = request.POST['event_name']
        description = request.POST['description']
        location = request.POST['location']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        registration_deadline = request.POST['registration_deadline']
        host_email = request.POST['host_email']
        host_password = request.POST['host_password']
        event_info = eventRegistration.objects.create(
            eventName = event_name,
            description = description,
            location = location,
            fromDate = from_date,
            toDate = to_date,
            registrationDeadline = registration_deadline,
            hostEmail = host_email,
            hostPassword = host_password
        )
        event_info.save()
        return render(request, 'event_registration_page.html')
        #return HttpResponse("Saved")

def participant_registration(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        content = {
            'events' : eventRegistration.objects.all(),
            'now' : now
        }
        return render(request, 'participant_registration_page.html', content)
    elif request.method == 'POST':
        participant_name = request.POST['participant_name']
        contact_no = request.POST['contact_no']
        participant_email = request.POST['participant_email']
        event_to_participate = request.POST['event_to_participate']
        registration_type = request.POST['registration_type']
        no_of_people = request.POST['no_of_people']
        participant_info = participantRegistration.objects.create(
            participantName = participant_name,
            contactNumber = contact_no,
            participantEmail = participant_email,
            eventName = event_to_participate,
            registrationType = registration_type,
            noOfPeople = no_of_people,
        )
        participant_info.save()
        #print(participant_name, contact_no, participant_email, event_to_participate, registration_type, no_of_people)
        now = datetime.datetime.now()
        content = {
            'events': eventRegistration.objects.all(),
            'now': now
        }
        return render(request, 'participant_registration_page.html', content)