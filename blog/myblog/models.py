#coding:utf-8
from django.db import models
from django.contrib.auth.models import User


#文章类别

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#文章标签

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#文章
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=70)
    #正文
    body = models.TextField()
    #创建时间
    create_time = models.DateTimeField()
    #最后一次修改时间
    modified_time = models.DateTimeField()
    #文章摘要
    excerpt = models.CharField(max_length=200,blank=True) #blank=True字段允许为空，默认不允许
    #浏览量
    views = models.IntegerField(default=0)
    #read = models.IntegerField(max_length=11,default=0,editable=True)
    
     #类外键（一对多）
    category = models.ForeignKey(Category)
    #标签对文章（多对多）
    tags = models.ManyToManyField(Tag,blank=True)
   
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。s.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)
    def __str__(self):
        return self.title


