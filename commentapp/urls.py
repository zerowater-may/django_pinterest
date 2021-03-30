from django.contrib import admin
from django.urls import path, include

# from .views import (ProfileCreateView , ProfileUpdateView)
from .views import CommentCreateView,CommentDeleteView
app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]