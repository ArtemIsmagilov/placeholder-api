import json

from django.core.management.base import BaseCommand
from placeholder_api.models import User, Comment, Post, Todo, Album, Photo


class Command(BaseCommand):
    help = "Init DB from Placeholder json file"

    def handle(self, *args, **options):
        data = json.load(open("data.json"))

        users = (
            User(
                id=u["id"],
                name=u["name"],
                username=u["username"],
                email=u["email"],
                address=" ".join(
                    (
                        u["address"]["street"],
                        u["address"]["suite"],
                        u["address"]["city"],
                        u["address"]["zipcode"],
                        u["address"]["geo"]["lat"],
                        u["address"]["geo"]["lng"],
                    )
                ),
                phone=u["phone"],
                website=u["website"],
                company=" | ".join(
                    (
                        u["company"]["name"],
                        u["company"]["catchPhrase"],
                        u["company"]["bs"],
                    )
                ),
            )
            for u in data["users"]
        )
        User.objects.bulk_create(users)

        todos = (
            Todo(
                id=t["id"],
                title=t["title"],
                completed=t["completed"],
                user_id=t["userId"],
            )
            for t in data["todos"]
        )
        Todo.objects.bulk_create(todos)

        albums = (
            Album(
                id=a["id"],
                title=a["title"],
                user_id=a["userId"],
            )
            for a in data["albums"]
        )
        Album.objects.bulk_create(albums)

        photos = (
            Photo(
                id=p["id"],
                title=p["title"],
                url=p["url"],
                thumbnail_url=p["thumbnailUrl"],
                album_id=p["albumId"],
            )
            for p in data["photos"]
        )
        Photo.objects.bulk_create(photos)

        posts = (
            Post(id=p["id"], title=p["title"], body=p["body"], user_id=p["userId"])
            for p in data["posts"]
        )
        Post.objects.bulk_create(posts)

        comments = (
            Comment(
                id=c["id"],
                name=c["name"],
                email=c["email"],
                body=c["body"],
                post_id=c["postId"],
            )
            for c in data["comments"]
        )
        Comment.objects.bulk_create(comments)

        self.stdout.write(
            self.style.SUCCESS("Successfully init tables from placeholder json.")
        )
