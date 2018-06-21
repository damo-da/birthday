from django.contrib import admin


class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'article', 'literature_from')
    empty_value_display = '-empty-'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @classmethod
    def reset_heroes(cls):
        print('resetting heroes')
        return ''


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'hero', 'gender', 'w_number', 'birth_date')
    empty_value_display = '-empty-'


class EmailMasterAdmin(admin.ModelAdmin):
    list_display = ('given_name', 'display_name', 'email', 'updated_on')
    readonly_fields = ('refresh_token', 'email')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

