from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=10, primary_key=True)
    hall = models.CharField(max_length=20)
    contact = models.IntegerField()
    exp = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.roll