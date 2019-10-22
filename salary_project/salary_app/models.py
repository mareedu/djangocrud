from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=40)
    salary = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.company + " " + str(self.salary)
