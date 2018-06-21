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

from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

ARTICLE_CHOICES = (
    ('a', 'a'),
    ('an', 'an'),
    ('the', 'the'),
)


class SuperHero(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    article = models.CharField(max_length=3, choices=ARTICLE_CHOICES)
    literature_from = models.CharField(max_length=200, blank=True, default='')
    desc = models.CharField(max_length=2000, blank=True, default='')
    
    def __str__(self):
        return self.name

    def get_title(self):
        ret = self.name

        if self.literature_from:
            ret += ' from ' + self.literature_from

        if self.desc:
            ret += ', ' + self.desc

        return ret

class Person(models.Model):
    hero = models.ForeignKey(SuperHero)
    
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, default='')
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    w_number = models.CharField(max_length=8, blank=True, default='')
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name()
    
    def name(self):
        if self.middle_name:
            return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)
        else:
            return '{} {}'.format(self.first_name, self.last_name)


class EmailMaster(models.Model):
    given_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    email = models.EmailField()

    refresh_token = models.TextField()
    updated_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} <{}>'.format(self.display_name, self.email)
