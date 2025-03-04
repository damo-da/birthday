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

from django.contrib import admin

from .models import SuperHero, Person, EmailMaster, Log
from .admin_models import SuperHeroAdmin, PersonAdmin, EmailMasterAdmin, LogEntryAdmin

admin.site.register(Person, PersonAdmin)
admin.site.register(SuperHero, SuperHeroAdmin)
admin.site.register(EmailMaster, EmailMasterAdmin)
admin.site.register(Log, LogEntryAdmin)

