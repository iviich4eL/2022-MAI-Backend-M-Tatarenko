from django.contrib import admin

# Register your models here.

# lab 5
from .models import Creator, Post

class CreatorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "nickname")
    list_filter = ("name",)

admin.site.register(Creator, CreatorAdmin)
admin.site.register(Post)