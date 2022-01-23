from django.contrib import admin
from django.urls import path
from . import views
from login.views import PersonFormView

urlpatterns = [
    path('', views.home, name='home'),
    path('login', PersonFormView.as_view(), name='login'),
    path('login_done', views.login_done, name='login_done'),
    path('wellcome', views.wellcome, name='wellcome'),
]
