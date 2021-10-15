from django.contrib import admin

# Register your models here.
from .models import Sex


class SexAdmin(admin.ModelAdmin):
    list_display = ('sex_user', 'created')
    list_display_links = ('sex_user',)
    search_fields = ('sex_user',)
    list_per_page = 25


admin.site.register(Sex, SexAdmin)
