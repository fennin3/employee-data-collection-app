from django.db import models
from django.db.models.fields import IntegerField


class Supervisor(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    age = models.IntegerField()
    dateofbirth = models.DateField()
    date_of_employment = models.DateField(default="2017-04-09")
    position = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    salary = IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    date_of_birth = models.DateField(help_text="format: yy-mm-dd (eg. 2020-12-14)")
    date_of_employment = models.DateField(
        help_text="format: yy-mm-dd (eg. 2020-12-14)",
    )
    position = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    salary = IntegerField()
    supervisors = models.ManyToManyField(
        Supervisor,
        verbose_name=("supervisors"),
        related_name="employees",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    number_of_employee_data = models.IntegerField()
    status = models.CharField(max_length=15)
    error = models.CharField(max_length=100)