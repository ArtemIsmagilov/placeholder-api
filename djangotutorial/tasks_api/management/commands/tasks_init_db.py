import random

from django.core.management.base import BaseCommand

from tasks_api.models import (
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


class Command(BaseCommand):
    help = "Init tasks db with random data"

    def handle(self, *args, **options):
        statuses = [
            Status(name=name, is_close=is_close, description=desc)
            for name, is_close, desc in [
                ("New", False, "Task just created"),
                ("In Progress", False, "Task is being worked on"),
                ("Done", True, "Task completed"),
                ("Closed", True, "Task closed"),
            ]
        ]
        Status.objects.bulk_create(statuses)

        priorities = [
            Priority(name=name, active=active)
            for name, active in [
                ("Low", True),
                ("Medium", True),
                ("High", True),
                ("Critical", True),
            ]
        ]
        Priority.objects.bulk_create(priorities)

        categories = [Category(name=f"Category {i}") for i in range(5)]
        Category.objects.bulk_create(categories)

        roles = [Role(name=name) for name in ["Admin", "Manager", "Developer", "Viewer"]]
        Role.objects.bulk_create(roles)

        groups = [Group(name=name) for name in ["Alpha", "Beta", "Gamma"]]
        Group.objects.bulk_create(groups)

        projects = [
            Project(
                identifier=f"PRJ-{i}",
                name=f"Project {i}",
                description=f"Description for project {i}",
                is_public=random.choice([True, False]),
            )
            for i in range(5)
        ]
        Project.objects.bulk_create(projects)

        users = [
            User(
                login=f"user{i}",
                admin=random.choice([True, False]),
                firstname=f"First{i}",
                lastname=f"Last{i}",
                mail=f"user{i}@example.com",
                role=random.choice(roles),
                group=random.choice(groups),
            )
            for i in range(10)
        ]
        User.objects.bulk_create(users)

        tasks = [
            Task(
                subject=f"Task {i}",
                description=f"Description for task {i}",
                start_date=f"2025-01-{i % 28 + 1:02d}",
                due_date=f"2025-02-{i % 28 + 1:02d}" if random.choice([True, False]) else None,
                is_private=random.choice([True, False]),
                done_percent=random.randint(0, 100),
                closed_on=None,
                spent_days=random.randint(1, 10) if random.choice([True, False]) else None,
                estimated_days=random.randint(1, 15),
                category=random.choice(categories),
                assigned_to=random.choice(users),
                author=random.choice(users),
                priority=random.choice(priorities),
                status=random.choice(statuses),
                project=random.choice(projects),
            )
            for i in range(20)
        ]
        Task.objects.bulk_create(tasks)

        news_list = [
            News(
                title=f"News {i}",
                summary=f"Summary for news {i}",
                description=f"Full description of news item {i}",
                project=random.choice(projects),
                author=random.choice(users),
            )
            for i in range(10)
        ]
        News.objects.bulk_create(news_list)

        comments = [
            Comment(
                content=f"Comment {i} about something",
                author=random.choice(users),
                some_news=random.choice(news_list),
            )
            for i in range(30)
        ]
        Comment.objects.bulk_create(comments)

        self.stdout.write(
            self.style.SUCCESS("Successfully initialized tasks db with random data.")
        )
