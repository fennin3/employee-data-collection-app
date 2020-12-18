from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreation
from django.contrib import messages
from .models import Employee


@login_required
def home(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, "base/index.html", context)


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

def upload_data(request):
    return render(request, 'base/upload.html')
