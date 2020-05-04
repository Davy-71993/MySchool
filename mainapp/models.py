from django.db.models import Q

from datetime import datetime, date, timedelta
from django.db import models
from .helper import week, get_dates, str_week_day

class Calendar(models.Model):
    year = models.IntegerField(unique=True)
    today = date.today()

    def __str__(self):
        return f'{ self.year }'

    @property
    def last_term(self):
        ct = self.current_term.name
        if ct == 'First Term':
            return None
        elif ct == 'Second Term':
            return Term.objects.get(name = 'First Term', year = datetime.now().year)
        elif ct == 'Third Term':
            return Term.objects.get(name = 'Second Term', year = datetime.now().year)
        elif 'Holidays' in ct:
            if self.current_term.name == 'First Term Holidays':
                return Term.objects.get(name = 'First Term', year = datetime.now().year)
            elif self.current_term.name == 'Second Term Holidays':
                return Term.objects.get(name = 'Second Term', year = datetime.now().year)
            elif self.current_term.name == 'Third Term Holidays':
                return Term.objects.get(name = 'Third Term', year = datetime.now().year)
    
    @property
    def next_term(self):
        ct = self.current_term.name
        if ct == 'First Term':
            return Term.objects.get(name = 'Second Term', year = datetime.now().year)
        elif ct == 'Second Term':
            return Term.objects.get(name = 'Third Term', year = datetime.now().year)
        elif ct == 'Third Term':
            return None
        elif 'Holidays' in ct:
            if self.current_term.name == 'First Term Holidays':
                return Term.objects.get(name = 'Second Term', year = datetime.now().year)
            elif self.current_term.name == 'Second Term Holidays':
                return Term.objects.get(name = 'Third Term', year = datetime.now().year)
            elif self.current_term.name == 'Third Term Holidays':
                return None

    @property
    def current_term(self):
        t1 = Term.objects.get(name = 'First Term', year = self.year)
        t2 = Term.objects.get(name = 'Second Term', year = self.year)
        t3 = Term.objects.get(name = 'Third Term', year = self.year)
        
        if str(self.today) in get_dates(t1.fro_date, t1.to_date):
            return t1
        elif str(self.today) in get_dates(t2.fro_date, t2.to_date):
            return t2
        elif str(self.today) in get_dates(t3.fro_date, t3.to_date):
            return t3
        elif str(self.today) in get_dates(t1.to_date, t2.fro_date):
            holidays = self.holidays(name = 'First Term Holidays', fro_date = t1.to_date, to_date = t2.fro_date)
            events = Event.objects.none()
            dates = get_dates(holidays.fro_date, holidays.to_date)
            for d in dates:
                q = Event.objects.filter(fro_date = d)
                events |= q
            holidays.events = events.order_by('fro_date')
            return holidays
        elif str(self.today) in get_dates(t2.to_date, t3.fro_date):
            holidays =self.holidays(name = 'Second Term Holidays', fro_date = t1.to_date, to_date = t2.fro_date)
            return holidays
        elif str(self.today) in get_dates(t3.to_date, date(datetime.now().year, 12, 31)):
            holidays = self.holidays(name = 'Third Term Holidays', fro_date = t1.to_date, to_date = t2.fro_date)
            return holidays
        elif str(self.today) > date(datetime.now().year, 1, 1):
            holidays = self.holidays(name = "New Year's Holidays", fro_date = date(datetime.now().year, 1, 1))
            return holidays

    def holidays(self, name, fro_date, to_date = None):
        return Event(name = name, fro_date = fro_date, to_date = to_date)
    
    @property
    def events_today(self):
        yr = datetime.now().year
        mn = datetime.now().month
        d = datetime.now().day
        return Event.objects.filter(fro_date = date(yr, mn, d))

    @property
    def events_this_week(self):
        fd = week()[0]
        ld = week()[1]
        dates = get_dates(fd, ld)

        events = Event.objects.none()

        for d in dates:
            q = Event.objects.filter(fro_date = d)
            events |= q

        return events.order_by('fro_date')

    @property
    def events_this_month(self):
        first_day_of_month = date(datetime.now().year, datetime.now().month, 1)
        today = date.today()
        next_month = today.replace(day=28) + timedelta(days=4)# get next month
        last_day_of_month = next_month - timedelta(days=next_month.day)# subtruct all the days of next month to get the last day

        dates = get_dates(first_day_of_month, last_day_of_month)
        events = Event.objects.none()

        for d in dates:
            q = Event.objects.filter(fro_date = d)
            events |= q
        
        return events.order_by('fro_date')

    @property
    def events_this_year(self):
        yr = datetime.now().year
        first_day = date(yr, 1, 1)
        last_day = date(yr, 12, 31)

        dates = get_dates(first_day, last_day)
        events = Event.objects.none()

        for d in dates:
            q = Event.objects.filter(fro_date = d)
            events |= q

        return events.order_by('fro_date')

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    fro_date = models.DateField()
    fro_time = models.TimeField()
    to_date = models.DateField(blank=True, null=True)
    to_time = models.TimeField(blank=True, null=True)
    events = None

    def __str__(self):
        return self.name

    @property
    def day(self):
        today = date.today()
        if self.fro_date == today:
            return 'Today'
        elif self.fro_date.day == today.day + 1 and self.fro_date > today:
            return 'Tomorrow'

        elif self.fro_date.day == today.day - 1 and today > self.fro_date:
            return 'Yesterday'
        else:
            return str_week_day(self.fro_date)

class Term(Event):
    year = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def events(self):
        es = Event.objects.none()
        fd = self.fro_date
        ld = self.to_date

        dates = get_dates(fd, ld)
        for d in dates:
            q = Event.objects.filter(fro_date = d).exclude(fro_date = self.fro_date, to_date = self.to_date)
            es |= q
        return es.order_by('fro_date', 'fro_time')


