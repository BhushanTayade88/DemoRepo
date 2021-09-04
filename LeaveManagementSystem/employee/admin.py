from django.contrib import admin
from .models import Role,Department
# Register your models here.

@admin.register(Role)
class AdminRole(admin.ModelAdmin):
    list_display = ['name','description','created','updated']

@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    list_display = ['name','description','created','updated']

