from django.contrib import admin

# Register your models here.
from .models import Date


class DateAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_user', 'created')
    list_display_links = ('title', 'date_user')
    search_fields = ('title', 'date_user')
    list_per_page = 25


admin.site.register(Date, DateAdmin)
