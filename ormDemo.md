## orm入门知识
#### Book和Publisher多对一的关系
#### 在属于多的类里面创外键   
```models.py
from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    publisher = models.ForeignKey('Publisher', related_name='person_book', related_query_name='yy')

```
```
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'showbook$',views.showbook, name='showbook')
]

```

```
from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from prac.models import Publisher, Book

# Create your views here.

def showbook(request):
    # dict={}

    #正向查找  多--->少     书到出版社
    # ob = Book.objects.all()  #取到书籍对象
    # for item in ob:
    #     print(item.person.id)
    # dict['name']=item.name


    #反向查找   少----->多   出版社到书
    # ob = Publisher.objects.first()
    # ob = Publisher.objects.get(id=1)

    # # ret = ob.person_book.all()   #如果用了person_book就用定义好的person_book的值
    # ret = ob.book_set.all()        #如果没有定义就用类名的 首字母小写的类名_set
    # titles = ret.values_list('name')
    # print('======this is bookname:',titles)
    # return HttpResponse('hi,showbook')

    # ob = Publisher.objects.first()
    # book = ob.person_book.all()
    # titles = book.values_list('name')
    # print('======this is bookname:',titles)
    # return HttpResponse('hi,showbook')


    # print(ret, type(ret))
    # for i in ret:
    #     print(i.name)
    
    #跨表查询
    ob = Book.objects.filter(id=1).values(book__name)
    print('this is ob:', ob)
    return HttpResponse('hi,showbook')

    # ret = Publisher.objects.filter(id=1).values_list('yy__name')
    # print('this is =================ret:', ret)
    # return HttpResponse('hi,showbook')

```
一对多
一是主表
多是子表


[查看原文](https://www.cnblogs.com/aaronthon/p/9520832.html)
理解ORM:[查看原文](https://www.cnblogs.com/welan/p/9858747.html)
