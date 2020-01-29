## django之跨表查询及添加记录 

#### 关于_set写法，是否已经有些晕了，究竟什么时候使用_set,简单记忆，只有子表才有"子表名小写_set"的写法，得到的是一个QuerySet集合，后边可以接.add(),.remove(),.update(),.delete(),.clear()
*****




一：创建表
书籍模型： 书籍有书名和出版日期，一本书可能会有多个作者，一个作者也可以写多本书，所以作者和书籍的关系就是多对多的关联关系(many-to-many);
一本书只应该由一个出版商出版，所以出版商和书籍是一对多关联关系(one-to-many)。
创建一对一的关系：OneToOne("要绑定关系的表名")
创建一对多的关系：ForeignKey("要绑定关系的表名")
创建多对多的关系：ManyToMany("要绑定关系的表名")  会自动创建第三张表


```子子母   母子子  出版社publish是主表    book是子表

类名.objects.create()
增加：
一对多：
Book.objects.create(title="追风筝的人", publishDdata="2015-5-8", price="111", publish_id=1)
一对一：
AuthorDeital.objects.create(tel='654321', addr='SH', author_id=2)
多对多：
    #这就包含了增与改的用法
    #从Book出发   就是Book类里面定义了authorlist的多对多关系
	
    # 写法：某一子表对象.子表多对多字段.add(*主QuerySet对象)
    #Author是主表  Book是子表   
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
    #写法：某一母表对象.子表名小写_set.add(子表对象)
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
```	
	
```	
	
删：
一对多：
    #对于主表就只有一种情况，就是自己删自己就好
    # Publish.objects.get(name='复旦出版社').delete()

    #对于子表要分成两种情况
    # 1.自己删自己表里面的内容
    # 2.跨表删 （删除出版社是人大出版社的所有书）
    # Book.objects.get(title='go').delete()
    # Book.objects.filter(publish__name='人大出版社').delete()  #删除人大出版社出版的所有书


一对一：
    #########删主表 就可以了

    # Author.objects.filter(name='xiaowuwu').delete()  #删主表的某一行数据会将子表相应的数据也删掉
    # AuthorDeital.objects.filter(addr='GY').delete()  #删子表的某一行数据只会删掉子表的内容，删不了主表的

多对多：
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
```
```
	
 改：
一对多：
    #对于主表就只有一种情况，就是自己修改自己就好
    # Publish.objects.filter(name='人大出版社').update(name='人大人大出版社')

    #对于子表要分成两种情况
    # 1.自己修改自己表里面的内容
    # 2.跨表修改 （修改出版社是人大出版社的所有书的publish_id, 相当于就是改变出版社）

    # Book.objects.filter(title='go').update(price = '99.00')
    # Book.objects.filter(publish__name='人大出版社').update(publish_id=2)

一对一：
    #分成两种情况，1.改变自己表中的内容。 2.跨表改变表中的内容
    #######对于2.跨表修改的话     开始要和结束是同一张表的

    # Author.objects.filter(authordeital__tel=123456).update(name='xiaowuwu')   #可行
    # Author.objects.filter(name='xiaowuwu').update(authordeital__addr='bj')      #不可行
    # AuthorDeital.objects.filter(addr='SH').update(author__name='xun')   #不可行
    AuthorDeital.objects.filter(author__name='xiaoxun').update(addr='shanghai')  #可行

多对多：
	和增加在一起
	
```
```
查：
一对多：
    # 一对多查询记录：
    # 正向查询(按字段：publish)： 正向查询是查到主表的内容 正查主
    # 反向查询(按表名：book_set)： 反向查询是查到子表的内容	反查子

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
一对一：
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


多对多：
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

```





删除母表数据:
如果是一对一或者一对多关系，删除主表，子表对应数据会自动删除。
多对多关系，删除主表，主表_子表数据会自动删除，但是子表对应数据不会自动删除。
如果想要一对多关系中栓除主表数据，保留子表数据，那需要在子表建表时加入以下字段：

```
class Clothes(models.Model):
 color=models.ForeignKey("Colors",null=True,on_delete=models.SET_NULL)) #可为空，如果外键被删后，子表数据此字段置空而不是直接删除这条数据，同理也可以SET_DEFAULT,需要此字段有默认值
 description=models.CharField(max_length=10) #描述 

```

[查看原文](https://www.jb51.net/article/161232.htm)
[查看原文](https://www.cnblogs.com/chichung/p/9905835.html)
[查看原文](https://www.jb51.net/article/166288.htm)
[查看原文](https://www.cnblogs.com/morgana/p/8492895.html)
[ORM](https://www.cnblogs.com/welan/p/9858747.html)
[Template高级应用](https://www.cnblogs.com/believepd/p/9879473.html)
[open()](https://www.runoob.com/python/python-func-open.html)
##### 正查主  反查子

***********************************************
pycharm的快捷键
1. ctrl+end  快速跳到尾部
2. ctrl+home 快速跳到头部


