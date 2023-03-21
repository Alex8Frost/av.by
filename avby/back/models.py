from django.db import models
from back import constants


class TransportMark(models.Model):
    name = models.CharField(max_length=30, verbose_name='Марка', unique=True)

    class Meta:
        verbose_name = 'Марка транспорта'
        verbose_name_plural = 'Марки транспорта'

    def __str__(self):
        return self.name


class TransportModel(models.Model):
    name = models.CharField(max_length=32, verbose_name='Модель', unique=True)
    mark = models.ForeignKey(TransportMark, on_delete=models.CASCADE, verbose_name='Марка')

    class Meta:
        verbose_name = 'Модель транспорта'
        verbose_name_plural = 'Модели транспорта'

    def __str__(self):
        return f'{self.name} {self.mark.name}'


class TransportAd(models.Model):
    mark = models.ForeignKey(TransportMark, on_delete=models.CASCADE, related_name='marks', verbose_name='Марка')
    model = models.ForeignKey(TransportModel, on_delete=models.CASCADE, related_name='models', verbose_name='Модель')
    type_of_transport = models.CharField(max_length=32, choices=constants.TypeOfTransport,
                                         verbose_name='Тип транспорта')
    year = models.IntegerField(verbose_name='Год')
    price_in_dollar = models.IntegerField(verbose_name='Цена')
    engine = models.CharField(max_length=32, choices=constants.TypeOfEngine, verbose_name='Двигатель')
    engine_capacity = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Объем двигателя')
    drive_unit = models.CharField(max_length=32, choices=constants.TypeOfDriveUnit, verbose_name='Привод')
    mileage = models.IntegerField(verbose_name='Пробег')
    vin_number = models.CharField(max_length=17, null=True, blank=True, verbose_name='ВИН номер')
    status = models.CharField(max_length=16, choices=constants.TransportAdStatus, verbose_name='Статус')
    description = models.TextField(max_length=500, verbose_name='Описание')
    post_date = models.DateTimeField(auto_now=True, verbose_name='Дата подачи')
    close_date = models.DateTimeField(verbose_name='Дата снятия')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.mark} {self.model.name}'
