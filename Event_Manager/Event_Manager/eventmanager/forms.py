from .models import event_registration
from django import forms
from django.forms import DateTimeInput
from django.contrib.admin.widgets import AdminSplitDateTime, AdminDateWidget, AdminTimeWidget


#class event_registration_form(forms.ModelForm):
    #host_password = forms.CharField(widget=forms.PasswordInput(attrs={
    #    'data-target': '#password'
    #}))
    #host_email = forms.EmailField(widget=forms.EmailInput(attrs={
    #    'data-target': '#email'
    #}))
    #event_name = forms.CharField(
    #    widget=forms.TextInput(attrs={
    #            'data-target': '#event_name'
    #        }
    #    )
    #)
    #description = forms.CharField(
    #    widget=forms.Textarea(attrs={
    #        'data-target': '#description',
    #        'cols': 30,
    #        'rows': 3
    #    }
    #    )
    #)
    #location = forms.CharField(
    #    widget=forms.TextInput(attrs={
    #        'data-target': '#location'
    #    }
    #    )
    #)
    #from_date = forms.DateTimeField(
    #    input_formats=['%d/%m/%Y %H:%M'],
    #    widget=forms.DateTimeInput(attrs={
    #        'class': 'form-control datetimepicker-input',
    #        'data-target': '#datetimepicker1'
    #    }))
    #to_date = forms.DateTimeField(
    #    input_formats=['%d/%m/%Y %H:%M'],
    #    widget=forms.DateTimeInput(attrs={
    #        'class': 'form-control datetimepicker-input',
    #        'data-target': '#datetimepicker2'
    #    }))
    #registration_deadline = forms.DateTimeField(
    #    input_formats=['%d/%m/%Y %H:%M'],
    #    widget=forms.DateTimeInput(attrs={
    #        'class': 'form-control datetimepicker-input',
    #        'data-target': '#datetimepicker3'
    #    }))
    #class Meta:
    #    model = event_registration
    #    exclude = ()