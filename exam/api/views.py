from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
	TokenAuthentication,
	SessionAuthentication
)

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from exam.models import Exam, Question

from exam.api.serializers import *

class QuestionApiView(ListAPIView):
	queryset = Question.objects.root_nodes().prefetch_related("children")
	serializer_class = QuestionSerializer
	authentication_classes = () 
	permission_classes = ()
	pagination_class = PageNumberPagination
	filter_backends = (SearchFilter, OrderingFilter)