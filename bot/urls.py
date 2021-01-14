from django.contrib import admin
from django.urls import path

from .views import bot, get_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', bot, name='bot'),
    path('bot/get-response/', get_response),
]