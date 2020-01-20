## django之跨表查询及添加记录 

#### 关于_set写法，是否已经有些晕了，究竟什么时候使用_set,简单记忆，只有子表才有"子表名小写_set"的写法，得到的是一个QuerySet集合，后边可以接.add(),.remove(),.update(),.delete(),.clear()
*****


一：创建表
书籍模型： 书籍有书名和出版日期，一本书可能会有多个作者，一个作者也可以写多本书，所以作者和书籍的关系就是多对多的关联关系(many-to-many);
一本书只应该由一个出版商出版，所以出版商和书籍是一对多关联关系(one-to-many)。
创建一对一的关系：OneToOne("要绑定关系的表名")
创建一对多的关系：ForeignKey("要绑定关系的表名")
创建多对多的关系：ManyToMany("要绑定关系的表名")  会自动创建第三张表

```

```

[](https://www.jb51.net/article/161232.htm)
[](https://www.cnblogs.com/chichung/p/9905835.html)