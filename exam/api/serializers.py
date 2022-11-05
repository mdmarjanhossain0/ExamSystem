from rest_framework import serializers

from exam.models import Exam, Question

import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from rest_framework_recursive.fields import RecursiveField



class QuestionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Question
        fields = ['id', 'name', 'options', 'answer',  'type', 'exam', 'children']