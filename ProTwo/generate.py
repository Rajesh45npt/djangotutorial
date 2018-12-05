import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from faker import Faker
from AppTwo.models import User

fakegen = Faker()

def generate(N=5):
    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()
        User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print('generating data')
    generate(20000)
    print("generating complete")
