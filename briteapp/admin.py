from django.contrib import admin
from .models import Favourite, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Favourite)