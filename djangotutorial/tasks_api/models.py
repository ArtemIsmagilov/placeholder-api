from django.db import models
from django.db.models import UniqueConstraint, CheckConstraint, Q, F


class Status(models.Model):
    name = models.CharField()
    is_close = models.BooleanField(default=False)
    description = models.CharField(null=True, blank=True)


class Priority(models.Model):
    name = models.CharField()
    active = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField()


class Role(models.Model):
    name = models.CharField()


class Group(models.Model):
    name = models.CharField()


class Project(models.Model):
    identifier = models.CharField()
    name = models.CharField()
    description = models.CharField()
    is_public = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["name", "parent"], name="unique_name_per_parent"),
            CheckConstraint(
                condition=~Q(id=F("parent")), name="prevent_self_parent_for_projects"
            ),
        ]


class User(models.Model):
    login = models.CharField()
    admin = models.BooleanField()
    firstname = models.CharField()
    lastname = models.CharField()
    mail = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Task(models.Model):
    subject = models.CharField()
    description = models.CharField()
    start_date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    is_private = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    done_percent = models.IntegerField(default=0)
    closed_on = models.DateTimeField(null=True, blank=True)
    spent_days = models.IntegerField(null=True, blank=True)
    estimated_days = models.IntegerField(null=True, blank=True)

    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assigned_tasks"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_tasks"
    )
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            CheckConstraint(
                condition=Q(done_percent__gte=0) & Q(done_percent__lte=100),
                name="done_percent_range_0_100",
            ),
            CheckConstraint(
                condition=~Q(id=F("parent")), name="prevent_self_parent_for_tasks"
            ),
        ]


class News(models.Model):
    title = models.CharField()
    summary = models.CharField()
    description = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    some_news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="comments"
    )
