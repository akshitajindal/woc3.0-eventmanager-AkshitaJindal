from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from .models import eventRegistration
from .models import participantRegistration
import datetime
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
import django.contrib.messages
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
        poster_link = request.POST['poster_link']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        registration_deadline = request.POST['registration_deadline']
        host_email = request.POST['host_email']
        host_password = request.POST['host_password']
        event_info = eventRegistration.objects.create(
            eventName = event_name,
            description = description,
            location = location,
            posterLink = poster_link,
            fromDate = from_date,
            toDate = to_date,
            registrationDeadline = registration_deadline,
            hostEmail = host_email,
            hostPassword = host_password
        )
        event_info.save()
        subject = 'Event Successfully Registered'
        message = "You've registered your event "+event_name+": "+description+". To be held at "+location+".\n"\
        +"Your event would last from: "+from_date+" to "+to_date+".\n"\
        +"The last date to register is: "+registration_deadline+".\n"\
        +"You can view the poster for your event at: "+poster_link+"\n"\
        +"Your event id is: "+host_email+" and your event password is: "+host_password+".\n"\
        +"Thank you for registering your event on our website."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [host_email,]
        send_mail(subject, message, email_from, recipient_list)
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
        now = datetime.datetime.now()
        same_email = participantRegistration.objects.filter(participantEmail=request.POST['participant_email']).values()
        count = len(same_email)
        flag = 0
        if count > 0:
            for obj in same_email:
                if obj['eventId']==int(request.POST['event_to_participate']):
                    messages.error(request, "You've already registered for this event.")
                    flag = 1
                    break
        if flag == 0:
            participant_name = request.POST['participant_name']
            contact_no = request.POST['contact_no']
            participant_email = request.POST['participant_email']
            event_id = request.POST['event_to_participate']
            event = eventRegistration.objects.get(id=event_id)
            event_to_participate = event.eventName
            registration_type = request.POST['registration_type']
            no_of_people = request.POST['no_of_people']
            participant_info = participantRegistration.objects.create(
                participantName=participant_name,
                contactNumber=contact_no,
                participantEmail=participant_email,
                eventId=event_id,
                eventName=event_to_participate,
                registrationType=registration_type,
                noOfPeople=no_of_people,
            )
            # print(participant_name, contact_no, participant_email, event_to_participate, registration_type, no_of_people)
            participant_info.save()
            account_sid = 'ACa0dd67152cf2a834c5aad1f265dadaa9'
            auth_token = '042b4089383c9cf3d874dda84eb90910'
            client = Client(account_sid,auth_token)
            client.messages.create(
                to = '+91'+contact_no,
                from_ = '+13392090590',
                body="Hello "+participant_name+", you've been successfully registered for the event "
                +event.eventName+": "+event.description+". To be held at "+event.location+".\n"
                + "The event would last from: " + str(event.fromDate) + " to " + str(event.toDate) + ".\n"
                + "You can view the event poster at: " + event.posterLink + "\n"
                +"Your participant id is: "+str(participant_info.id)+"\n"
                +"The email you used to register is: "+participant_email+"\n"
                +"Registeration type: "+registration_type+"\n"
                +"Number of people: "+str(no_of_people)+"\n"
                +"Hope you have have a good time."
            )
        content = {
            'events': eventRegistration.objects.all(),
            'now': now,
        }
        return render(request, 'participant_registration_page.html', content)

def event_dashboard(request):
    if request.method=='GET':
        return render(request, 'event_dashboard.html')
    elif request.method=="POST":
        if eventRegistration.objects.filter(id=request.POST['event_id']).exists():
            if eventRegistration.objects.get(id=request.POST['event_id']).hostPassword==request.POST['host_password'] and eventRegistration.objects.get(id=request.POST['event_id']).hostEmail==request.POST['host_email']:
                participants = participantRegistration.objects.filter(eventId = request.POST['event_id'])
                if len(participants)>0:
                    content = {
                        'participants': participants,
                    }
                    return render(request,'event_dashboard.html',content)
                else:
                    messages.info(request,'We did not receive any participation for your event.')
                    return render(request,'event_dashboard.html')
            else:
                messages.error(request,"The email or password you entered is incorrect!")
                return render(request,'event_dashboard.html')
        else:
            messages.error(request,"No event is registered with this eventId.")
            return render(request,'event_dashboard.html')