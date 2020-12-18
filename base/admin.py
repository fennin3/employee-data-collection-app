from django.contrib import admin
from .models import Supervisor, Employee, Log

# Register your models here.

admin.site.register(Supervisor)
admin.site.register(Employee)
admin.site.register(Log)
