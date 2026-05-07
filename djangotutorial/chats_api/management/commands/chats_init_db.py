import random

from django.core.management.base import BaseCommand

from chats_api.models import User, Chat, Message


class Command(BaseCommand):
    help = "Init db from dummy json files"

    def handle(self, *args, **options):
        us = [User(username=f"user {i}") for i in range(10)]
        User.objects.bulk_create(us)

        cs = [Chat(name=f"chat {i}") for i in range(100)]
        Chat.objects.bulk_create(cs)
        for c in cs:
            c.users.set(random.sample(us, random.randint(1, len(us))))

        ms = [
            Message(
                chat=random.choice(cs),
                author=random.choice(us),
                text=f"message {i}",
            )
            for i in range(1000)
        ]
        Message.objects.bulk_create(ms)

        self.stdout.write(
            self.style.SUCCESS("Successfully init db from random module.")
        )
