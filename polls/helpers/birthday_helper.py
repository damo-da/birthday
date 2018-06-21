from __future__ import print_function
import datetime
import random
from polls.models import EmailMaster, SuperHero
from mysite import settings

print('reading pi...', end='')
with open('data/pi.txt') as f:
    pi = f.read()
print('pi read')


def number_of_days_since_birth(birth_date):
    today = datetime.datetime.today().date()
    diff = birth_date - today
    return abs(diff).days


def index_in_pi(number):
    number = str(number)
    return pi.index(number) + 1


def get_random_superhero(gender):
    gender = gender.upper()

    this_gender_heros = SuperHero.objects.filter(gender=gender)
    hero = random.choice(this_gender_heros)
    return hero


def get_template_params(person):

    num_days_since_birth = number_of_days_since_birth(person.birth_date)
    hero = person.hero
    emailMaster = EmailMaster.objects.first()

    data = {
        'first_name': person.first_name,
        'full_name': person.name(),
        'my_donation_amount': settings.DONATION_AMOUNT,
        'superhero': hero.get_title(),
        'superhero_article': hero.article,
        'pi_index': index_in_pi(num_days_since_birth),
        'num_days_since_birth': num_days_since_birth,
        'to_email': person.email ,
        'from_email': emailMaster.email,
        'from_name': emailMaster.display_name
    }

    return data


if __name__ == '__main__':
    print(get_random_superhero('F'))