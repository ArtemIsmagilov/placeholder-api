from django.db import models


class User(models.Model):
    name = models.CharField()
    username = models.CharField()
    email = models.EmailField()
    address = models.CharField()
    phone = models.CharField()
    website = models.CharField()
    company = models.CharField()


class Todo(models.Model):
    title = models.CharField()
    completed = models.BooleanField()

    user = models.ForeignKey("User", on_delete=models.CASCADE)


class Album(models.Model):
    title = models.CharField()

    user = models.ForeignKey("User", on_delete=models.CASCADE)


class Photo(models.Model):
    title = models.CharField()
    url = models.URLField()
    thumbnail_url = models.URLField()

    album = models.ForeignKey("Album", on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField()
    body = models.TextField()

    user = models.ForeignKey("User", on_delete=models.CASCADE)


class Comment(models.Model):
    name = models.CharField()
    email = models.EmailField()
    body = models.TextField()

    post = models.ForeignKey("Post", on_delete=models.CASCADE)
