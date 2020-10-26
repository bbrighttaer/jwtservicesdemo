# Author: bbrighttaer
# Project: bookservice
# Date: 10/26/2020
# Time: 7:43 PM
# File: serializers.py

from __future__ import absolute_import, division, print_function, unicode_literals

from .models import Book
from rest_framework import serializers


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'percent_completed', 'category', 'date']
