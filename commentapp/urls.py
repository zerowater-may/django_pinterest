from django.contrib import admin
from django.urls import path, include

# from .views import (ProfileCreateView , ProfileUpdateView)
from .views import CommentCreateView
app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
]