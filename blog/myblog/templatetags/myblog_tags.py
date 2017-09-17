from ..models import Post,Category,Tag
from django import template

#最新文章
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


#归档模板标签（实现按月归档的目的）
@register.simple_tag
def archives():
    return Post.objects.dates('create_time','month',order='DESC')


#分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def  get_tag():
    return Tag.objects.all()

