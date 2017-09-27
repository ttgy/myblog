#coding:utf-8
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from django.urls import reverse
# Create your views here.

from comments.forms import CommentForm

import markdown

from .models import Post,Category

#首页
def index(request):
    #return HttpResponse('hello world!')
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,'index.html',context={'post_list':post_list})


#详情页
def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    #导入CommentForm
    form =  CommentForm()
    #获取这篇post 下的全部评论
    comment_list = post.comments_set.all().order_by('-created_time')
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list
    }
    return render(request, 'detail.html', context=context)


#归档
def archives(request, year, month):
    if int(month) < 10:
        month = '0'+month
    post_list = Post.objects.filter(create_time__startswith=year+'-'+month).order_by('-create_time')
                #Entry.objects.filter(pub_date__month=12)
    print(post_list)
    return render(request, 'index.html', context={'post_list': post_list})


#分类
def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    print(cate)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    print(post_list)
    return render(request, 'index.html', context={'post_list': post_list})

def aaa(request):
     return render(request, 'index.html')

