from django.contrib import admin
from .models import Todolist, Todo
# Register your models here.

admin.site.register(Todolist)
admin.site.register(Todo)