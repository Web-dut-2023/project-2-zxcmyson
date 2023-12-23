from django.db import models

class Users(models.Model):
    username = models.CharField(verbose_name='姓名', max_length=32, null=True, blank=True)
    password = models.CharField(verbose_name='密码', max_length=32, null=True, blank=True)
    watch = models.CharField(verbose_name='监视名单', max_length=32, null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.password})"

class goods_list(models.Model):
    name = models.CharField(verbose_name='商品名', max_length=32, null=True, blank=True)
    publisher = models.CharField(verbose_name='发布者', max_length=32, null=True, blank=True)
    category = models.CharField(verbose_name='商品类别', max_length=32, null=True, blank=True)
    price = models.CharField(verbose_name='价格', max_length=32, null=True, blank=True)
    introduction = models.CharField(verbose_name='商品介绍', max_length=32, null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/',null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
class price_list(models.Model):
    name = models.CharField(verbose_name='商品名', max_length=32, null=True, blank=True)
    pidname = models.CharField(verbose_name='出价者名字', max_length=32, null=True, blank=True)
    price = models.CharField(verbose_name='价格', max_length=32, null=True, blank=True)

    def __str__(self):
        return f"{self.name}/{self.pidname}({self.price})"


class comment(models.Model):
    name = models.CharField(verbose_name='商品名', max_length=32, null=True, blank=True)
    commentname = models.CharField(verbose_name='评论者名字', max_length=32, null=True, blank=True)
    article = models.CharField(verbose_name='评论内容', max_length=32, null=True, blank=True)

    def __str__(self):
        return f"{self.name}/{self.commentname}"