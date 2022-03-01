
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Student_list, name='Student_list'),
    path('not/', views.studentList, name='studentList'),
    path('indi/', views.studentList2, name='studentList2'),
    path('search/<str:name>', views.searchName, name='Student_search')

]
