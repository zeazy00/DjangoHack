"""
Definition of urls for DjangoHack.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('app.urls')),
]
