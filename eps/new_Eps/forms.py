from dataclasses import fields
from django import forms
from .models import User,Appointment,Doctor

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields='__all__'
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields='__all__'