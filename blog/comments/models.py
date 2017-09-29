#from django.db import models

# Create your models here.
from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)

    url = models.URLField(blank=True)
    text = models.TextField()
    #auto_now_add 指定为当前的时间
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('myblog.Post')

    def __str__(self):
        return self.text[:20]



