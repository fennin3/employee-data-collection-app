from os import error
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreation
from django.contrib import messages
from .models import Employee, Supervisor, Log
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
from task.tasks import upload_task
from task.tasks import message_


@login_required
def home(request):
    employees = reversed(Employee.objects.all())
    context = {"employees": employees}
    return render(request, "base/index.html", context)


@login_required
def log(request):
    logs = reversed(Log.objects.all())
    context = {"logs": logs}
    return render(request, "base/logs.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect("home")
        else:
            return render(request, "base/login.html")
    return render(request, "base/login.html")


@login_required
def employee_creation(request):
    if request.method == "POST":
        form = EmployeeCreation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully")
            return redirect("home")
        else:
            messages.error(request, "Please check input")
            form = EmployeeCreation()
            return render(request, "base/create_employee.html", {"form": form})
    else:
        form = EmployeeCreation()
        return render(request, "base/create_employee.html", {"form": form})


@login_required
def upload_data(request):
    if request.method == "POST":
        try:
            file_ = request.FILES["file"]
        except Exception as e:
            file_ = ""
        filename = str(file_)
        ext = filename.split(".")[-1]

        print(ext)
        if ext == "xlsx":
            upload_task(file_)
            return redirect("home")
        elif ext == "":
            messages.error(request, "Please choose a file")
        else:
            messages.error(
                request, "Please upload an Excel file with '.xlsx' extension"
            )
            return redirect("upload_data")
    return render(request, "base/upload.html")
