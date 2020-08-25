from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(unique=True,max_length=16,verbose_name='用户名字')
    password=models.CharField(max_length=32,verbose_name='用户密码')
    class Meta:
        db_table='user'


class Blog(models.Model):
    content=models.CharField(max_length=512,verbose_name='博客内容')
    user_id=models.ForeignKey(User,blank=True,null=True)

    class Meta:
        db_table='blog'



class Comment(models.Model):
    review=models.CharField(max_length=256,verbose_name='评论内容')
    c_user=models.ForeignKey(User,blank=True,null=True)
    c_blog=models.ForeignKey(Blog,blank=True,null=True)

    class Meta:
        db_table='comment'