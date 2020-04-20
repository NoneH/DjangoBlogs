from datetime import datetime
from django.db import models

# from users.models import UserProfile

# Create your models here.


class Blog(models.Model):
    """
    博客
    """
    # user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    title = models.CharField(verbose_name=u'标题', max_length=32)
    author = models.CharField(verbose_name=u'作者', max_length=16)
    content = models.TextField(verbose_name=u'博客正文')
    catagory = models.CharField(max_length=10, choices=(('yw', '英文'), ('hz', '汉子')), verbose_name='分类')
    tags = models.CharField(max_length=20, verbose_name='标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"博客"
        verbose_name_plural = verbose_name


class Comments(models.Model):
    # user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name=U"博客", on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def __str__(self):
        return self.comments

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name
