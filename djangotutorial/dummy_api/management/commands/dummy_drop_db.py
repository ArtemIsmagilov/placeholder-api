
from django.core.management.base import BaseCommand

from dummy_api.models import (
    User,
    Todo,
    Recipe,
    Quote,
    Product,
    Review,
    Post,
    Comment,
    Cart,
)


class Command(BaseCommand):
    help = "Drop tables from dummy app"

    def handle(self, *args, **options):
        User.objects.all().delete()

        Todo.objects.all().delete()

        Recipe.objects.all().delete()

        Quote.objects.all().delete()

        Product.objects.all().delete()

        Review.objects.all().delete()

        Post.objects.all().delete()

        Comment.objects.all().delete()

        Cart.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Successfully truncate dummy tables."))
