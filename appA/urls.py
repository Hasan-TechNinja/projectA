from django.urls import path
from . import views

urlpatterns = [
    path('all/<int:pk>', views.studentData, name='student'),
    path('all/', views.AllStudentData, name='student'),
]
