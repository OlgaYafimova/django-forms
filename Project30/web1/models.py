from django.db import models

class MyModel(models.Model):
    surname = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.surname}"