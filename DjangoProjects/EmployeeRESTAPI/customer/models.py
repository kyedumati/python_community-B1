from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name


