from django.core.management.base import BaseCommand

from tasks_api.models import (
    Comment,
    News,
    Task,
    User,
    Project,
    Group,
    Role,
    Category,
    Priority,
    Status,
)


class Command(BaseCommand):
    help = "Drop all records from tasks app tables"

    def handle(self, *args, **options):
        Comment.objects.all().delete()
        News.objects.all().delete()
        Task.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()
        Group.objects.all().delete()
        Role.objects.all().delete()
        Category.objects.all().delete()
        Priority.objects.all().delete()
        Status.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Successfully dropped all tasks data."))
