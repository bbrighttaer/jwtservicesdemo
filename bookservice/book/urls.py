# Author: bbrighttaer
# Project: bookservice
# Date: 10/26/2020
# Time: 7:41 PM
# File: urls.py

from __future__ import absolute_import, division, print_function, unicode_literals
from django.urls import path
from .views import BookDetailAPIView, BookListAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('<int:id>/', BookDetailAPIView.as_view(), name='book_detail')
]
