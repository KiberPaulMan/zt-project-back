from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    is_active = serializers.BooleanField(source='user.is_active')

    class Meta:
        model = Employee
        exclude = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data.get('password'))
        user.save()

        employee = Employee.objects.create(user=user, **validated_data)
        employee.save()

        return employee

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        User.objects.filter(id=instance.user.id).update(**user_data)
        return super().update(instance, validated_data)

