from django.db import models


# Create your models here.
class Class(models.Model):
    g_name = models.CharField(max_length=18, default='3年级１班')
    g_boy_num = models.IntegerField(default=0)
    g_girl_num = models.IntegerField(default=0)


# 重写objects=models.Manager()
class MyManager(models.Manager):
    def get_queryset(self):
        return super(MyManager, self).get_queryset().exclude(isDelete=True)

    def createModel(self, name, age=18, sex=1):
        student = self.model()
        student.s_name = name
        student.s_age = age
        student.s_sex = sex
        return student


class Student(models.Model):
    s_name = models.CharField(max_length=20)
    s_age = models.IntegerField(default=18)
    s_sex = models.BooleanField(default=0)

    # 调用重写的objects覆盖默认的objects=models.Manager()
    objects = MyManager()
    isDelete = models.BooleanField(default=False)
