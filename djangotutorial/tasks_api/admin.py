from django.contrib import admin

from .models import (
    Status,
    Priority,
    Category,
    Role,
    Group,
    Project,
    User,
    Task,
    News,
    Comment,
)


admin.site.register(Status)
admin.site.register(Priority)
admin.site.register(Category)
admin.site.register(Role)
admin.site.register(Group)
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Task)
admin.site.register(News)
admin.site.register(Comment)
