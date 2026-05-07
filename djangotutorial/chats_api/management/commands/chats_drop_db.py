from django.core.management.base import BaseCommand

from chats_api.models import User, Chat, Message


class Command(BaseCommand):
    help = "Drop tables from chats app"

    def handle(self, *args, **options):
        User.objects.all().delete()

        Chat.objects.all().delete()

        Message.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Successfully truncate chats tables."))
