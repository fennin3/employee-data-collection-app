from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("create-employee/", views.employee_creation, name="create_employee"),
    path("upload-employee-data/", views.upload_data, name="upload_data"),
    path('upload-logs/', views.log, name="log")
]
