from django.db import models

# CREATE TABLE STUDENT(FIRST_NAME VARCHAR(20),LAST_NAME VARCHAR(30),EMAIL_ID VARCHAR(30))
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name

class Employee(models.Model):
    ename=models.CharField(max_length=30)
    empno = models.CharField(max_length=30)
    email_id = models.CharField(max_length=60)

    def __str__(self):
        return self.ename


