from django.contrib import admin

# Register your models here.
from .models import Photo, Category

admin.site.register(Photo)
admin.site.register(Category)