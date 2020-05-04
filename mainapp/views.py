from datetime import datetime, date

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import SignupForm, SubjectForm, PaperForm, CalendarForm
from .models import Calendar, Event, Term
from .helper import get_dates, str_week_day
from students.models import Subject, Paper

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'The user name or password is incorrect, Please try again')
    context = {}
    return render(request, 'mainapp/login.html', context)

def signout(request):
    logout(request)
    return redirect('login')

def signup(request):
    form = SignupForm()

    if(request.method == 'POST'):
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'mainapp/signup.html', context)

def create_calendar(request):
    cl = Calendar.objects.filter(year = datetime.datetime.now().year)
    if request.method == 'POST':
        cl = Calendar.objects.filter(year = request.POST.get('year'))
        if cl.count():
            pass
        else:
            form = CalendarForm(request.POST)
            if form.is_valid():
                form.save()
    
    context = {
        'calendar': cl,
        'yr': datetime.datetime.now().year,
    }
    return render(request, 'mainapp/create_calendar.html', context)

def calendar(request):
    cl = Calendar.objects.get(year=datetime.now().year)
    terms = Term.objects.filter(year = cl.year)
    events = None
    target = ''
    if request.GET.get('where'):
        where = request.GET.get('where')
        if where == 'today':
            events = cl.events_today
            target = 'Today'
        elif where == 'week':
            events = cl.events_this_week
            target = 'This Week'
        elif where == 'month':
            events = cl.events_this_month
            target = 'This Month'
        elif where == 'term':
            events = cl.current_term.events
            s = cl.current_term.name
            if 'Holidays' in s:
                target = 'This Holidays'
            else:
                target = 'This Term'
        elif where == 'year':
            events = terms
    print(cl.next_term)
    context = {
        'calendar': cl,
        'events': events,
        'target': target,
    }
    return render(request, 'mainapp/calender.html', context)

def setup_calendar(request):
    fro_date = date.today
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        fro_date = request.POST.get('fro_date')
        fro_time = request.POST.get('fro_time')
        to_date = request.POST.get('to_date') or fro_date
        to_time = request.POST.get('to_time') or fro_time

        Event.objects.create(
            name =name,
            description = description,
            fro_date = fro_date,
            fro_time = fro_time,
            to_date = to_date,
            to_time = to_time
        )
    cl = Calendar.objects.get(year = datetime.now().year)
    context = {
        'calendar': cl,
        'name': fro_date,
    }
    return render(request, 'mainapp/setup_calendar.html', context)

def home(request):
    return render(request, 'mainapp/home.html')

def admindashboard(request):
    return render(request, 'mainapp/admindashboard.html')

def subjects(request):
    subs = Subject.objects.all()
    sub_form = SubjectForm()

    if request.method == 'POST':
        sub_form = SubjectForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            pass

    context ={
        'subjects': subs,
        'subject_form': sub_form,
    }

    return render(request, 'mainapp/subjects.html', context)

def add_paper(request, pk, px):
    subject = Subject.objects.get(id = pk)
    paper_form = PaperForm()
    paper_form.fields['subject'].value = subject
    if request.method == 'POST':
        paper_form = PaperForm(request.POST)
        if paper_form.is_valid():
            paper_form.save()
            return redirect('subjects')

    context ={
        'subject': subject,
        'level': px,
        'paper_form': paper_form,
    }
    return render(request, 'mainapp/add_paper.html', context)

def update_subject(request, pk):
    subject = Subject.objects.get(id = pk)
    form = SubjectForm(instance=subject)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects')

    context = {
        'form':form,
        'instance': subject,
    }
    return render(request, 'mainapp/update.html', context)

def delete_subject(request, pk):
    subject = Subject.objects.get(id = pk)

    if request.method == 'POST':
        subject.delete()
        return redirect('subjects')

    context ={
        'instance': subject,
        'object': 'Subject'
    }
    return render(request, 'mainapp/delete.html', context)

def edit_paper(request, pk):
    paper = Paper.objects.get(id = pk)
    form = PaperForm(instance=paper)

    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect('subjects')

    context = {
        'form':form,
        'instance': paper,
    }
    return render(request, 'mainapp/update.html', context)

def delete_paper(request, pk):
    paper = Paper.objects.get(id = pk)

    if request.method == 'POST':
        paper.delete()
        return redirect('subjects')

    context ={
        'instance': paper,
        'object': 'Paper'
    }
    return render(request, 'mainapp/delete.html', context)






