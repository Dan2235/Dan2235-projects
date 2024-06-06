from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=25)
    channel_name = models.CharField(max_length=25)
    subscribers = models.IntegerField(default=0)
    password = models.CharField(max_length=25)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField()
    likes = models.IntegerField(default=0)

class PostsCount(models.Model):
    count = models.IntegerField()