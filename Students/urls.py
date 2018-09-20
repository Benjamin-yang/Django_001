from django.urls import path

from Students import views

app_name='students'
urlpatterns=[
    path('', views.index, name='index')
]