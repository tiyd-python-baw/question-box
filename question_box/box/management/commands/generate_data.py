from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from box.models import Score


def generate_users():
    from faker import Faker
    fake = Faker()
    user_list = [x for x in {fake.user_name() for _ in range(500)}]
    count = 0
    for _ in range(50):
        user = User.objects.create_user(user_list[count],password='password',email=fake.email())
        user.save()
        score = Score(user=user)
        score.save()
        count += 1



def generate_questions():
    import json
    from faker import Faker
    import random
    from .list_gen import q_list
    fake = Faker()
    questions=[]
    for x in range(50):
        question = {'fields':{'title':q_list[x],
                            'text':fake.bs(),
                            'timestamp':str(fake.date_time_this_year()),
                            'user': random.choice(range(1,51)),
                            },
                    'model':'box.Question',}
        questions.append(question)
    with open('./box/fixtures/questions.json', 'w') as f:
        f.write(json.dumps(questions))

def generate_answers():
    import json
    from faker import Faker
    import random
    fake = Faker()
    answers = []
    for _ in range(50):
        answer = {'fields':{'text':fake.bs(),
                            'timestamp':str(fake.date_time_this_year()),
                            'user': random.choice(range(1,51)),
                            'question':random.choice(range(1,51))
                            },
                    'model':'box.Answers',}
        answers.append(answer)
    with open('./box/fixtures/answers.json', 'w') as f:
        f.write(json.dumps(answers))

def generate_tags():
    import json
    tags = []
    from .tag_list import tag_list
    for x in range(len(tag_list)):
        tag = {'fields':{'name':tag_list[x]},
                'model':'box.Tag'}
        tags.append(tag)
    with open('./box/fixtures/tags.json','w') as f:
        f.write(json.dumps(tags))


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_users()
        # generate_questions()
        # generate_answers()
        # generate_tags()
