# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import print_function
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Person, EmailMaster
from .helpers.birthday_helper import get_template_params
from .helpers.email_helper import send_email
import datetime
from helpers.log import log
from mysite.settings import TIME_ZONE
import pytz


def index(request):
    return HttpResponse("This site is no longer working. Bye.")


def test(request):
    return HttpResponse('done')


def send_birthday_emails(request):
    tz = pytz.timezone(TIME_ZONE)
    now = datetime.datetime.now(tz)

    todays_birthday_persons = Person.objects\
        .filter(birth_date__month=now.month,
                birth_date__day=now.day)\
        .all()

    if todays_birthday_persons.count() == 0:
        return HttpResponse('no birthdays today.')
    else:
        admin = EmailMaster.objects.first()
        msg = ''
        for person in todays_birthday_persons:
            if person.last_birthday_email_sent_on_year < now.year:

                data = get_template_params(person)

                template = render_to_string('polls/happy_birthday_email.html', data)

                send_email(admin.email, person.email, 'Happy birthday!', template)

                send_email(admin.email, admin.email, 'BIRTHDAY: {} on {}'.format(person, person.birth_date), '')

                person.last_birthday_email_sent_on_year = now.year
                person.save()
                msg += 'Happy Birthday, {}! '.format(person)

                log('Birthday email for {} was sent at {}. '.format(person, now))
            else:
                msg += 'Birthday email for a person was already sent. <br />'.format(person)
        return HttpResponse(msg)





