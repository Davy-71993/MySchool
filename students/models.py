import datetime
from django.db import models
# from mainapp.helper import allocate_house


class Subject(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=6)
    alevel = models.BooleanField(default= False)
    olevel = models.BooleanField(default= False)
    olevel_code = models.CharField(max_length=10, blank=True, null=True)
    alevel_code = models.CharField(max_length=10, blank=True, null=True)
    is_compulsary = models.BooleanField(default=False)

    @property
    def olevel_papers(self):
        return Paper.objects.filter(subject = self, level = 'Olevel')

    @property
    def alevel_papers(self):
        return Paper.objects.filter(subject = self, level = 'Alevel')

    def __str__(self):
        return self.name

class Paper(models.Model):
    level_choices = (
        ('Alevel', 'Alevel'),
        ('Olevel', 'Olevel')
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.CharField(max_length= 10, choices= level_choices)

    def __str__(self):
        return f'{self.subject} {self.name}'

class Student(models.Model):
    class_choices = (
        ('S.1', 'S.1'),
        ('S.2', 'S.2'),
        ('S.3', 'S.3'),
        ('S.4', 'S.4'),
        ('S.5', 'S.5'),
        ('S.6', 'S.6'),
    )

    streams = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('S', 'S'),
    )

    sex_choices = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )

    house_choices = (
        ('Australia', 'Australia'),
        ('Brazil', 'Brazil'),
        ('Canada', 'Canada'),
        ('France', 'France'),
        ('Japan', 'Japan'),
        ('Nigeria', 'Nigeria')
    )

    sir_name = models.CharField(max_length=50)
    given_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=8, choices=sex_choices)
    passport_photo = models.ImageField(upload_to='passports', blank=True, null=True)
    klass = models.CharField(max_length=5, choices=class_choices)
    stream = models.CharField(max_length=10, choices=streams)
    house = models.CharField(max_length=10, choices=house_choices, blank=True, null=True)
    # subjects = models.ManyToManField(Subject, default= Subject.objects.filter(is_compulsary=True))
    date_added = models.DateTimeField(auto_now=True)
    scores = {}

    def __str__(self):
        return self.sir_name

    @property
    def full_names(self):
        if self.other_names != None:
            return f'{self.sir_name} {self.given_name} {self.other_names}'

        else:
            return f'{self.sir_name} {self.given_name}'

    @property
    def subjects(self):
        alevel_classes = ['S.5', 'S.6']
        if self.klass in alevel_classes:
            return Subject.objects.filter(alevel = True)
        else:
            return Subject.objects.filter(olevel = True)

        
