from django.contrib import admin

# Register your models here.
from .models import Discussion


class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')
    list_display_links = ('title', 'user')
    search_fields = ('title', 'user')
    list_per_page = 25


admin.site.register(Discussion, DiscussionAdmin)
