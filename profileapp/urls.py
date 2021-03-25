from django.contrib import admin
from django.urls import path, include

from .views import (ProfileCreateView , ProfileUpdateView)

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]