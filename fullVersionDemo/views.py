from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from fullVersionDemo.models import Publish, Book, Author, AuthorDeital
# Create your views here.
#========================OneToMany Demo===========================================================

def addbook(request):
    #第一种方法
    # publisher_obj = Publish.objects.get(name = '人大出版社')
    # print(publisher_obj.id)
    # Book.objects.create(title='从零基础学python', publishDdata='2019-11-11', price='39.20', publish=publisher_obj)

    # 第二种方法
    Book.objects.create(title="追风筝的人", publishDdata="2015-5-8", price="111", publish_id=1)
    Book.objects.create(title='java', publishDdata='2014-12-12', price='32.00',publish_id=1)
    Book.objects.create(title='go', publishDdata='2011-1-12', price='15.00', publish_id=2)
    Book.objects.create(title='c#', publishDdata='2014-2-15', price='18.00', publish_id=1)
    Book.objects.create(title='c++', publishDdata='2018-2-20', price='32.00', publish_id=4)
    return HttpResponse('hi, add')

def deletebook(request):
    #对于主表就只有一种情况，就是自己删自己就好
    # Publish.objects.get(name='复旦出版社').delete()

    #对于子表要分成两种情况
    # 1.自己删自己表里面的内容
    # 2.跨表删 （删除出版社是人大出版社的所有书）
    # Book.objects.get(title='go').delete()
    # Book.objects.filter(publish__name='人大出版社').delete()  #删除人大出版社出版的所有书

    return HttpResponse('Hi, delete')

def updatebook(request):
    #对于主表就只有一种情况，就是自己修改自己就好
    # Publish.objects.filter(name='人大出版社').update(name='人大人大出版社')

    #对于子表要分成两种情况
    # 1.自己修改自己表里面的内容
    # 2.跨表修改 （修改出版社是人大出版社的所有书的publish_id, 相当于就是改变出版社）

    # Book.objects.filter(title='go').update(price = '99.00')
    # Book.objects.filter(publish__name='人大出版社').update(publish_id=2)

    return HttpResponse('hi, update')

def showbook(request):
    # 一对多查询记录：
    # 正向查询(按字段：publish)： 正向查询是查到主表的内容
    # 反向查询(按表名：book_set)： 反向查询是查到子表的内容

    #正向查询 查到 名为xxx这本书（子表）的出版社名字（主表的内容）
    #1.查找出名为xxx的这本书的对象
    #2. 在这本书对象.publish.name(相当于对象的属性的属性）  的出版社名字
    # book_obj =Book.objects.get(nid=3)
    # print(book_obj.nid, book_obj.publishDdata, type(book_obj))
    # print(book_obj.publish.name)

    #反向查询  查到某个出版社  所出版的  全部书
    #1.查到这个出版社对象
    #2. 出版社对象.book_set.all()
    # publish_obj = Publish.objects.get(name = '人大出版社')
    # book_obj = publish_obj.book_set.all()
    # for item in book_obj:
    #     print(item.title)


    #跨表查询 开始和filter怎么组合都可以，但是values后面的参数需要带引号
    # res=Book.objects.filter(publish__name="清华出版社").values("price","title")
    # res=Book.objects.filter(title="c++").values('publish__id')

    # res=Publish.objects.filter(name="清华出版社").values("book__price", "book__title")
    res=Publish.objects.filter(book__title="c#").values('name')

    print('=============res:',res)
    return HttpResponse('hi, show')

#=========================OneToMany Demo End=================================
def addAuthDetail(request):
    Author.objects.create(name='xiaoxun', age=16)
    Author.objects.create(name='xiaoli', age=15)
    AuthorDeital.objects.create(tel='654321', addr='SH', author_id=2)
    AuthorDeital.objects.create(tel='333333', addr='GY', author_id=3)
    return HttpResponse('hi, addAuthDetail')

def deleteAuthDetail(request):
    return HttpResponse('hi, deleteAuthDetail')

def updateAuthDetail(request):
    return HttpResponse('hi, updateAuthDetail')



def showAuthDetail(request):
    #Author相当于主表
    # 一对一的查询
    # 正向查询：手机号为13245的作者的姓名  从写了关联的地方开始，如AuthorDeital，如Book
    deital_obj = AuthorDeital.objects.filter(tel="123456").first()
    print(deital_obj.author.name)

    # 反向查询：查询egon的手机号
    # egon_obj = Author.objects.filter(name="xiaoxun").first()
    # print(egon_obj.authordeital.tel)


    #跨表查询 和onetomany很类似  开始和filter怎么搭配都可以
    # res = Author.objects.filter(authordeital__addr='sh').values('name')
    # res = Author.objects.filter(name='xiaowu').values('authordeital__addr')
    # res = AuthorDeital.objects.filter(author__name='xiaowu').values('addr')
    res = AuthorDeital.objects.filter(addr='SH').values('author__name')

    print('------res:',res)

    return HttpResponse('hi, showAuthDetail')



#========================OneToOne Demo Begin=================================















#========================OneToOne Demo End===================================