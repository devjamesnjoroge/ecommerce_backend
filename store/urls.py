from django.urls import path
from .views import *



urlpatterns = [
    path('api/v1/users/', UserView.as_view(), name='users')
]