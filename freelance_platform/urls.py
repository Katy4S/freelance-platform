"""
WSGI config for freelance_platform project.

It exposes the WSGI callable as a module-level variable named "application".
"""

import os
from django.core.wsgi import get_wsgi_application
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freelance_platform.settings")
application = get_wsgi_application()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", include("orders.urls")),
]


def home(request):
    return HttpResponse("Welcome to the Freelance Platform!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", include("orders.urls")),
    path("", home, name="home"),
]
