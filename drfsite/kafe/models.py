from django.db import models


class Tables(models.Model):
    num = models.IntegerField(verbose_name='Номер стола')
    description = models.CharField(max_length=200, unique=True, verbose_name='Описание')
    maxGuests = models.IntegerField(verbose_name='Макс количество человек')
    guestsDef = models.IntegerField(default=0, verbose_name='Гостей', blank=True, null=True)
    guestsNow = models.IntegerField(default=0, verbose_name='Присутствует гостей')

    class Meta:
        ordering = ['id']
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

    def __str__(self):
        return str(self.num)


class Guests(models.Model):
    table = models.ForeignKey(Tables, on_delete=models.PROTECT, verbose_name='Стол')
    name = models.CharField(max_length=255, db_index=True, verbose_name='ФИО')
    isPresent = models.BooleanField(default=False, verbose_name='Присутствие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        ordering = ('name', 'created',)
        index_together = (('id',),)
        verbose_name = 'Гостя'
        verbose_name_plural = 'Гости'

    def __str__(self):
        return self.name
