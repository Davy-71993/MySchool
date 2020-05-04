from django.db import models 

class Massage(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
