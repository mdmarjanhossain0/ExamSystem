from django.urls import path

from exam.api.views import QuestionApiView

app_name = 'exam'

urlpatterns = [
	path('test', QuestionApiView.as_view(), name="detail"),
]