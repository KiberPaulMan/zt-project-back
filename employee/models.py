from django.db import models
from django.conf import settings


class Department(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='employee')
    middle_name = models.CharField(max_length=20,
                                   blank=True,
                                   null=True,
                                   verbose_name='Отчество')
    date_of_birth = models.DateField(auto_now_add=True,
                                     verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='employees/%Y/%m/%d/',
                              blank=True,
                              verbose_name='Фото')
    job_title = models.CharField(max_length=30,
                                 verbose_name='Должность')
    department = models.ForeignKey(Department,
                                   on_delete=models.PROTECT,
                                   verbose_name='Подразделение',
                                   related_name='employees')

    def __str__(self):
        return self.user.username
