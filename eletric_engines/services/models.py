from django.db import models

# Create your models here.


class Services(models.Model):
    address = models.CharField(max_length=32)
    stret = models.CharField(max_length = 150)
    number = models.IntegerField()
    zipe_code = models.CharField(max_length=8)
    reference = models.CharField(max_length=150)
    request_date = models.DateField()
    delivery_date = models.DateField()

    def __str__(self):
        return str(self.id)