from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from students.models import Student, Subject, Paper
from .models import Calendar, Event

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widget=forms.TextInput(attrs={'autofocus': False})


class StudentRegistraionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = '__all__'


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'