from django.core.management.base import BaseCommand
from placeholder_api.models import User, Comment, Post, Todo, Album, Photo


class Command(BaseCommand):
    help = "Drop DB"

    def handle(self, *args, **options):
        User.objects.all().delete()

        Todo.objects.all().delete()

        Album.objects.all().delete()

        Photo.objects.all().delete()

        Post.objects.all().delete()

        Comment.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Successfully truncate tables"))
