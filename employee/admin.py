from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee, Department


class EmployeeInline(admin.StackedInline):
    model = Employee


class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Department)
