from django.contrib import admin
from .models import Post, Photo, Category


admin.site.register(Post)
# Register your models here.
admin.site.register(Photo)

admin.site.register(Category)