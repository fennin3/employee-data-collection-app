from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("create-employee/", views.employee_creation, name="create_employee"),
    path("upload-employee-data/", views.upload_data, name="upload_data"),
    path("upload-logs/", views.log, name="log"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
