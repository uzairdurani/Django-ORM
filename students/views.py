from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q
# Create your views here.


def Student_list(request):
    posts = Student.objects.all()
    print(posts.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': posts})


def searchName(request, name):
    posts = Student.objects.filter(surname__startswith=name)
    return render(request, 'output.html', {'posts': posts})


# not query
def studentList(request):
    # posts = Student.objects.exclude(age=12) & Student.objects.exclude(
    #     firstname__startswith='Muhammed')
    posts = Student.objects.filter(~Q(firstname__startswith='Muhammed'))
    return render(request, 'output.html', {'posts': posts})


# select individual fields
def studentList2(request):
    # posts = Student.objects.values('firstname', 'surname')
    posts = Student.objects.filter(age=12).only('firstname', 'surname')
    return render(request, 'output.html', {'posts': posts})
