from django.urls import path

from Students import views

app_name = 'students'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'addclass/', views.addClass, name='addclass'),
    path(r'showclass/', views.showClass, name='showclass'),
    path(r'addstudent/', views.addStudent, name='addclass'),
    path(r'showstudents/', views.showStudents, name='showclass'),

]
