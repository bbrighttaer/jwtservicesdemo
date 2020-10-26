# Author: bbrighttaer
# Project: authservice
# Date: 10/23/2020
# Time: 5:00 AM
# File: urls.py

from __future__ import absolute_import, division, print_function, unicode_literals

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
