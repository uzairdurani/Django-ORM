
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Student_list, name='Student_list'),
    path('search/<str:name>', views.searchName, name='Student_search')
]
