from django.db import models
from students.models import Student, Subject, Paper

class MarkList(models.Model):
    year = models.IntegerField()
    term = models.CharField(max_length=10)
    klass = models.CharField(max_length=10)
    stream = models.CharField(max_length=10)

    def smt(self, x=0):
        return (self.year) + x

    @property
    def level(self):
        a = ['S.5', 'S.6']
        if self.klass in a:
            return 'A'
        else:
            return 'O'

    @property
    def students(self):
        if self.stream:
            return Student.objects.filter(klass=self.klass, stream=self.stream)
        else:
            return Student.objects.filter(klass=self.klass)

    def __str__(self):
        return f'{self.klass} {self.stream} {self.term} {self.year}'

class MarkListSetUp(models.Model):
    marklist = models.OneToOneField(MarkList, on_delete=models.CASCADE)
    include_papers = models.BooleanField(default=False)
    num_exams = models.IntegerField()

    def __str__(self):
        return f'{ self.marklist } SETUP'

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marklist = models.ForeignKey(MarkList, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    value1 = models.FloatField(blank=True, null=True)
    value2 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{ self.student } { self.subject } Score'

class Result(models.Model):
    marklist = models.ForeignKey(MarkList, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{ self.student }'s Marks"
    
    @property
    def scores(self):
        std_scores = Score.objects.filter(marklist = self.marklist, student = self.student)
        scores = []

        for score in std_scores:
            xml ={ 
                'subject': score.subject,
                'value': score.value,
                'value1': score.value1,
            }
            scores.append(xml)
        return scores

    @property
    def all_scores(self):
        std_scores = Score.objects.filter(marklist = self.marklist, student = self.student)
        scores = {
            'student': self.student,
        }

        for score in std_scores:
            xml ={ 
                score.subject.abbr: {
                    'subject': score.subject,
                    'value': score.value,
                    'value1': score.value1,
                },
            }
            scores.update(xml)
        return scores

    def scores_by_subject(self, subject):
        scores = Score.objects.get(marklist = self.marklist, subject = subject, student = self.student)
        return scores
    


