from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from box.models import Score, Question, Answers


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
    fake = Faker()
    questions=[]
    for _ in range(50):
        question = {'fields':{'title':'A title',
                            'text':'Some text',
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
        answer = {'fields':{'text':'Answer text',
                            'timestamp':str(fake.date_time_this_year()),
                            'user': random.choice(range(1,51)),
                            'question':random.choice(range(1,51))
                            },
                    'model':'box.Answers',}
        answers.append(answer)
    with open('./box/fixtures/answers.json', 'w') as f:
        f.write(json.dumps(answers))

class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_users()
        generate_questions()
        generate_answers()
