from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


class Year(models.Model):
    date = models.CharField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('date',)
        verbose_name = 'Год выпуска'
        verbose_name_plural = 'Год выпуска'

    def __str__(self):
        return f'{self.date}'

