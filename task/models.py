from django.utils import timezone
from django.db import models
from employee.models import Employee

DATE_END = timezone.now() + timezone.timedelta(days=3)


class Task(models.Model):
    STATUS = (
        ('new', 'Новая'),
        ('in_the_pipeline', 'В работе'),
        ('completed', 'Выполнена'),
    )
    PRIORITY = (
        ('low', 'Низкий'),
        ('middle', 'Средний'),
        ('high', 'Высокий'),
    )

    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    status = models.CharField(max_length=20,
                              choices=STATUS,
                              default='new',
                              verbose_name='Статус')
    priority = models.CharField(max_length=10,
                                choices=PRIORITY,
                                default='middle')
    date_start = models.DateField(verbose_name='Дата начала задачи',
                                  default=timezone.now)
    date_finish = models.DateField(verbose_name='Дата окончания задачи',
                                   default=DATE_END)
    supervisor = models.ForeignKey(Employee,
                                   on_delete=models.SET_NULL,
                                   related_name='supervisor_tasks',
                                   verbose_name='Руководитель',
                                   null=True)
    responsible = models.ManyToManyField(Employee,
                                         related_name='responsible_tasks',
                                         verbose_name='Ответственный')
    functional_group = models.ManyToManyField(Employee,
                                              related_name='func_group_tasks',
                                              verbose_name='Функциональная группа',
                                              blank=True)
    observers = models.ManyToManyField(Employee,
                                       related_name='observers_tasks',
                                       verbose_name='Наблюдатели',
                                       blank=True)

    def __str__(self):
        return self.title[:50]