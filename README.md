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