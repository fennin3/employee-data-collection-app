from django import forms
from django.db.models import fields
from .models import Employee

class EmployeeCreation(forms.ModelForm):
    class Meta:
        model=Employee
        fields = '__all__'