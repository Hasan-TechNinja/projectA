from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def studentData(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')


def AllStudentData(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')