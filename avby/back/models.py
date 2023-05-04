from back import constants
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from back.managers import MyUserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


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
    status = models.CharField(max_length=16, choices=constants.TransportAdStatus,
                              default=constants.TransportAdStatus.open, verbose_name='Статус')
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    post_date = models.DateTimeField(auto_now=True, verbose_name='Дата подачи')
    close_date = models.DateTimeField(verbose_name='Дата снятия', null=True, blank=True)
    body = models.CharField(max_length=32, null=True, choices=constants.TransportBody, verbose_name='Кузов')
    transmission = models.CharField(max_length=32, null=True,
                                    choices=constants.TransportTransmission, verbose_name='трансмиссия')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Продавец')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.mark} {self.model.name}'


class Image(models.Model):
    transport_ad = models.ForeignKey(TransportAd, on_delete=models.CASCADE, verbose_name='Объявление')
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.transport_ad

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
