import pandas
import numpy

from django.shortcuts import render, redirect
from mainapp import forms
from .models import Student, Subject
from mainapp.helper import allocate_house

def add(request):
    subjects = Subject.objects.all()
    form = forms.StudentRegistraionForm()

    if request.method == 'POST':
        if request.FILES.get('std_file'):
            return redirect('students')

        form = forms.StudentRegistraionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            '''
                Each time we create a student we need to check if this student's class stream has any marklist
                If so, then a result should be appended to the marklist for this student. 
            '''
            return redirect('register_student')

    context = {
        'form': form,
        'subjects': subjects,
    }
    return render(request, 'students/add.html', context)

def import_students(request):

    if request.method == 'POST':
        std_file = request.FILES['std_file']

        df = pandas.read_excel(std_file)
        df.fillna('')
        rows = len(df)
        print(df)

        i = 0
        while i < rows:
            df['Other Names'].fillna('', inplace=True)
            df['Sex'].fillna('', inplace=True)
            print(df['Other Names'][i])
            Student.objects.create(
                sir_name = df['Sir Name'][i],
                given_name = df['Given Name'][i],
                other_names = df['Other Names'][i],
                sex = df['Sex'][i],
                klass = df['Class'][i],
                stream = df['Stream'][i],
                house = allocate_house()
            )

            i += 1

    context = {}
    return render(request, 'students/import.html', context)

def students(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students/students.html', context)

def student(request, pk):
    student = Student.objects.get(id=pk)
    form = forms.StudentRegistraionForm(instance=student)

    if request.method == 'POST':
        form = forms.StudentRegistraionForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')

    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'students/student.html', context)

def delete_student(request, pk):
    student = Student.objects.get(id = pk)

    if request.method == 'POST':
        student.delete()
        return redirect('students')

    context ={
        'instance': student,
        'object': 'Student'
    }
    return render(request, 'mainapp/delete.html', context)

def view_by_class(request, cl):
    students = Student.objects.filter(klass = cl)

    context = {
        'students': students,
        'class': cl,
    }
    return render(request, 'students/view_by_class.html', context)

def view_by_stream(request, cl, strm):
    students = Student.objects.filter(klass = cl, stream = strm)

    context = {
        'students': students,
        'class': cl,
        'stream': strm,
    }
    return render(request, 'students/view_by_stream.html', context)

def view_by_house(request, hs):
    students = Student.objects.filter(house = hs)

    context = {
        'students': students,
        'hs': hs,
    }
    return render(request, 'students/view_by_house.html', context)

















