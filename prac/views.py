from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from prac.models import Publisher, Book

# Create your views here.

# def index(request):
    #一对多查询，根据subject查询学生
    ##正向查询
    ##1.查询java学科
def addbook(request):
    ob = Book()
    ob.id=3
    ob.name = 'learn to be happy'
    ob.publisher_id =3
    ob.save()

    return HttpResponse('hi, add')


def deletebook(request):
    ob= Book.objects.get(id=1)
    ob.delete()
    return HttpResponse('Hi, delete')

def updatebook(request):
    ob = Book.objects.filter(id=1).update(name = 'python')

    # ob.name = '我要学python'
    # ob.save()

    return HttpResponse('hi, update')

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
    # ob = Book.objects.filter(id=1).values(publisher__name)
    # print('this is ob:', ob)
    # return HttpResponse('hi,showbook')

    ret = Publisher.objects.filter(id=1).values_list('ooxx__name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ')
    print('======this is ret person_book_name:', ret)























































