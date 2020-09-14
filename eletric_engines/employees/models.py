from django.db import models

# Create your models here.


class Employyes(models.Model):
    officce = models.CharField(max_length=150)
    shedule = models.CharField(max_length=10)
    salary = models.FloatField()
    company_time = models.FloatField()
    contract = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)