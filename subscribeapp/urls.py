


from django.contrib import admin
from django.urls import path, include

from .views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
]