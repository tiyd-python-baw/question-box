from django.core.management.base import BaseCommand
from box.models import Question,  Tag

def link_tags():
    import random
    for question in Question.objects.all():
        num = random.randint(0,5)
        tags = {random.choice(Tag.objects.all()) for _ in range(num)}
        for tag in tags:
            question.tags.add(tag)
        question.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        link_tags()
