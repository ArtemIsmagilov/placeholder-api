from django.db import models


class User(models.Model):
    username = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    name = models.CharField()
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
