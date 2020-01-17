from django.db import models

# Create your models here.

# class subject
# class students
# class teachers

#科目和学生之间是一对多
#学生和老师之间是多对多

# class SUBJECT(models.Model):

#     name = models.CharField(max_length=50)
#     price = models.IntegerField()

#     def __str__(self):
#         return '{}-{}'.format(self.name, self.price)

# class STU(models.Model):
#     name = models.CharField(max_length=32)
#     age = models.IntegerField()
#     phone = models.CharField(max_length=32)

#     #多对一在多的一方创建外键，外键生成之后会自动添加_id
#     subject = models.ForeignKey(to='SUBJECT',on_delete=True)
#     def __str__(self):
#         return '{}-{}'.format(self.name, self.age)


# class TEACHER(models.Model):
#     name = models.CharField(max_length=32)
#     age = models.IntegerField()
#     phone = models.CharField(max_length=32)
#     salary = models.CharField(max_length=32)

#     #多对多，在任意类中创建均可
#     student=models.ManyToManyField(to='STU')
#     def __str__(self):
#         return '{}-{}'.format(self.name, self.age)




from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    publisher = models.ForeignKey('Publisher', related_name='person_book', related_query_name='yy')
