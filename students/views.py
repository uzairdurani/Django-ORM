from django.shortcuts import render
from .models import Student
from django.db import connection
# Create your views here.


def Student_list(request):
    posts = Student.objects.all()
    print(posts.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': posts})


def searchName(request, name):
    print(name)
    posts = Student.objects.filter(surname__startswith=name)
    return render(request, 'output.html', {'posts': posts})
