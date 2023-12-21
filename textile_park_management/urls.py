
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hr/', include('hr_management.urls')),
    path('', include('hr_management.urls')),
]





