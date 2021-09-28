from django.db import models

# Create your models here.

# create table python manage.py  makemigrations
# python manage.py  migrate


class Table(models.Model):
    date = models.DateField('Дата')
    title = models.CharField('Название', max_length=50)
    quantity = models.IntegerField('Количество',blank=True, null=True)
    distance = models.FloatField('Расстояние',blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Строку'
        verbose_name_plural = 'Таблица'