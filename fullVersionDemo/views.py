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
    # Author.objects.create(name='xiaoxun', age=16)
    # Author.objects.create(name='xiaoli', age=15)
    AuthorDeital.objects.create(tel='654321', addr='SH', author_id=2)
    AuthorDeital.objects.create(tel='333333', addr='GY', author_id=3)
    return HttpResponse('hi, addAuthDetail')

def deleteAuthDetail(request):
    #########删主表 就可以了

    # Author.objects.filter(name='xiaowuwu').delete()  #删主表的某一行数据会将子表相应的数据也删掉
    # AuthorDeital.objects.filter(addr='GY').delete()  #删子表的某一行数据只会删掉子表的内容，删不了主表的
    return HttpResponse('hi, deleteAuthDetail')

def updateAuthDetail(request):

    #分成两种情况，1.改变自己表中的内容。 2.跨表改变表中的内容
    #######对于2.跨表修改的话     开始要和结束是同一张表的

    # Author.objects.filter(authordeital__tel=123456).update(name='xiaowuwu')   #可行
    # Author.objects.filter(name='xiaowuwu').update(authordeital__addr='bj')      #不可行
    # AuthorDeital.objects.filter(addr='SH').update(author__name='xun')   #不可行
    AuthorDeital.objects.filter(author__name='xiaoxun').update(addr='shanghai')  #可行

    return HttpResponse('hi, updateAuthDetail')

def showAuthDetail(request):
    #Author相当于主表
    # 一对一的查询
    # 正向查询：手机号为13245的作者的姓名  从写了关联的地方开始，如AuthorDeital，如Book
    # deital_obj = AuthorDeital.objects.filter(tel="123456").first()
    # print(deital_obj.author.name)

    # 反向查询：查询egon的手机号  一对一反向查询，直接表名就可以，不用跟_set
    egon_obj = Author.objects.filter(name="xiaoxun").first()
    print(egon_obj.authordeital.tel)

    #

    #跨表查询 和onetomany很类似  开始和filter怎么搭配都可以
    # res = Author.objects.filter(authordeital__addr='sh').values('name')
    # res = Author.objects.filter(name='xiaowu').values('authordeital__addr')
    # res = AuthorDeital.objects.filter(author__name='xiaowu').values('addr')
    # res = AuthorDeital.objects.filter(addr='SH').values('author__name')

    # print('------res:',res)

    return HttpResponse('hi, showAuthDetail')

#========================OneToOne Demo Begin=================================

#========================ManyToMany Demo Begin=================================
#一本书可能会有多个作者，一个作者也可以写多本书，所以作者和书籍的关系就是多对多的关联关系(many-to-many)
#在models里面建立了作者和书的多对多关系   authorlist = models.ManyToManyField("Author")  #建立的多对多的关系

def addBookAuthor(request):
    #这就包含了增与改的用法
    #从Book出发   就是Book类里面定义了authorlist的多对多关系
    # 写法：子表对象.子表多对多字段.add(*主QuerySet对象)
    # 写法2：
    #1.在Book里面添加一本书，2.获取全部的author， 3.让所有的author都写了这本书
    # book_obj = Book.objects.create(title='let it go', publishDdata='2019-12-12', price=100, publish_id=4)
    # author_obj=Author.objects.all()
    # book_obj.authorlist.add(*author_obj)


    #1.用.get获取书对象  2. 用.clear清除以前关联  3.在书对象里面加入author对象

    #对于获取对象，get和filter都可以
    #get
    # book_obj = Book.objects.get(title='let it go')
    # author_obj = Author.objects.get(name='xiaoli')
    # # print(author_obj.name)
    # book_obj.authorlist.clear()
    # book_obj.authorlist.add(author_obj)

    #filter
    # book_obj = Book.objects.get(title='let it go')
    # author_obj = Author.objects.filter(name='xiaoli')
    # # print(author_obj.name)
    # book_obj.authorlist.clear()
    # book_obj.authorlist.add(*author_obj)

    #从author 出发   author是主表=============================================
    #写法：母表对象.子表名小写_set.add(子表对象)
    #filter
    # xiaoyan_obj=Author.objects.get(name='xiaoyan')
    # book_obj=Book.objects.filter(title='go')
    # xiaoyan_obj.book_set.add(*book_obj)

    #get
    # xiaoyan_obj=Author.objects.get(name='xiaoyan')
    # book_obj = Book.objects.get(title='go')
    # xiaoyan_obj.book_set.add(book_obj)

    author_obj = Author.objects.get(name='xiaoyan')
    book_obj = Book.objects.all()
    author_obj.book_set.add(*book_obj)

    return HttpResponse('hi, add')

def deleteBookAuthor(request):
    #删除子表与主表关联关系
    #子对象.子表多对多字段.clear()
    #让名为go的书不再 连接 任何作者
    # book_obj = Book.objects.get(title='go')
    # book_obj.authorlist.clear()

    #删除主表和子表的关联关系
    #主对象.子表名_set.clear()
    #让所有书不再是被xiaoyan所写
    # author_obj = Author.objects.get(name='xiaoyan')
    # author_obj.book_set.clear()

    #删除多对多表数据
    #删除子表数据

    #删除xiaoxun参与写的所有书   book表中对应的数据删掉了
    # book_author表中对应的数据也删掉了
    # author_obj = Author.objects.get(name='xiaoxun')
    # author_obj.book_set.all().delete()

    #删除主表数据 只会删除主表和 book_author 表中对应的数据条，子表不受影响
    Author.objects.filter(name='xiaoli').delete()

    return HttpResponse('hi, delete')

def updateBookAuthor(request):

    return HttpResponse('hi, update')

def showBookAuthor(request):
    # 多对多的查询
    # 正向查询：查询追风筝的人的这本书的所有的作者的姓名和年龄
    # book_obj = Book.objects.filter(title="追风筝的人")[0]
    # print(book_obj.authorlist.all().values("name", "age"))  # 这本书关联的所有作者对象的集合


    #反向查询：查询作者是haiyan的这个人出了哪几本书的信息
    # xiaoxun_obj = Author.objects.filter(name="xiaoxun")[0]
    # print("bookinfo====", xiaoxun_obj.book_set.all().values('title'))  # 与该作者关联的所有书对象的集合


    #跨表查询
    # ret = Author.objects.filter(name="xiaoxun").values("book__title")
    # ret = Author.objects.filter(book__title='java').values('name')
    # ret = Book.objects.filter(authorlist__name="xiaoxun").values("title")
    ret = Book.objects.filter(title='java').values('authorlist__name')
    print(ret)

    return HttpResponse('hi, show')


#========================ManyToMany Demo End===================================













#========================OneToOne Demo End===================================