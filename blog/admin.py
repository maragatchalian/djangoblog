# Use this to add, edit, and delete posts

from django.contrib import admin
from .models import Post # Post was defined in models.py

# Register your models here.
admin.site.register(Post)
