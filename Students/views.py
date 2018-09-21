import random

from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Students.models import Class, Student


def index(request):
    return render(request, 'index.html')


def addClass(request):
    class0 = Class()
    class0_num = random.randrange(1, 500)
    class0.g_name = '北京小学%d班' % class0_num
    num01 = random.randrange(-5, 5)
    class0.g_boy_num = class0_num / 2 - num01
    class0.g_girl_num = class0_num / 2 + num01
    class0.save()
    return HttpResponse('Add success %d' % class0_num)


def showClass(request):
    # 1，获取全部class
    # classes = Class.objects.all()

    # 2，筛选女生人数多余男生人数的班级，
    # F对象： 能进行数学运算
    # classes = Class.objects.filter(g_girl_num__gt=F('g_boy_num'))

    # 3，选取男生人数大于50的
    # classes = Class.objects.filter(g_boy_num__gt=50)

    # 4，同时满足2,3条件，即女生多余男生，且男生人数大于50
    # 使用两次筛选或者通过Q对象来实现， Q对象支持逻辑运算
    # classes = Class.objects.filter(g_boy_num__gt=50).filter(g_girl_num__gt=F('g_boy_num'))
    classes = Class.objects.filter(Q(g_boy_num__gt=5) & Q(g_girl_num__gt=F('g_boy_num')))

    data = {
        'classes': classes,
    }
    return render(request, 'showclass.html', context=data)


def addStudent(request):
    num = random.randrange(1, 100)
    # 运用已改写的objects的方法createModel，来创建学生
    student = Student.objects.createModel('Tom%d' % num)
    student.save()
    return HttpResponse('Tom添加成功%d' % num)


def showStudents(request):
    students = Student.objects.all()
    data = {
        'students': students,
    }
    return render(request, 'showStudent.html', context=data)
