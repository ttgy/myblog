from django.shortcuts import render,get_object_or_404,redirect
from myblog.models import Post
from .models import  Comments
from .forms import  CommentForm
def post_comment(request,post_pk):
    print(post_pk)
    #快捷函数 获取当前的文章 存在时 则获取 否则返回404
    post = get_object_or_404(Post,pk=post_pk)

    print(post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        #当调用form.is_valid()方法时 自动帮忙检测 表单是否符合格式要求
        if  form.is_valid():
            #commit=False 的作用 仅仅 利用表单的数据生成 Comment 模型类的时列
            #但还不 保存评论数到数据库
            comment = form.save(commit=False)
            #将评论和被评论的文章关联起来
            comment.post = post
            #最终将评论数据保存进数据库
            comment.save()
            #return redirect(post)
            return redirect('myblog:detail', pk=post_pk)
    else:
        #当数据不合法时
        print(777)
        comment_list = post.comments_set.all()
        context = {
            'post':post,
            'form':form,
            'comment_list':comment_list
        }
        return render(request,'detail.html',context=context)
    print(888)
    return redirect(post)









