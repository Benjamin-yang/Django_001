# Django
前端和后端
## 一， Django项目的环境基本设置
**1，创建Django项目， 公用模板文件夹templates， 静态文件夹static**
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates') # 公用模板配置 
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 静态文件
STATIC_URL = '/static/'

STATICFILE_URL = {
    os.path.join(BASE_DIR, 'static')
}





```

## 二， 创建APP， 并添加到项目中

*1, 创建app*
```
python manage.py startapp Students


# 更改setting文件
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Students_001',
]


```

## 三，开发流程

１，　明确需求，设计模型（数据表）

eg: 一个学生成绩系统
功能：
   
    学生基本信息展示
    学生档案
    学生成绩
    老师信息
    学生创建
    学生删除
学生表 students
```
id  name sex age class_id 
1   张三　 0  10   1

```
教师表 teacher

```
id  name    sex    age    科目
1   舒振国　  １     34     
```
科目表 Subject
```
id  name    
1   语文
2   数学
3   英语
4   物理
5   化学
6   生物
7   政治
8   历史
9   地理
10  体育
11  音乐
13  美术

```

班级表 class
```
id  name  students_num  语文老师　数学老师　
  
１  603      33             
 ```
 
 班级科目教师表
 ```
 id     科目_id ｃlass_id    teacher_id
 
 ```