from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 100)
    idcourse = models.IntegerField()

    def __str__(self) -> str:
        return self.name