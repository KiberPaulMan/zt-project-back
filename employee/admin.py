from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee


class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]