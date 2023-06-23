from django.utils import timezone
from django.db import models

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

    title = models.CharField(max_length=20, verbose_name='Наименование')
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
