from django.shortcuts import Student
from rest_framework.generics import ListAPIView
from djangobackend.api.serializers import StudentSerializer
# Create your views here.

class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer