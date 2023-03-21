# Generated by Django 4.1.7 on 2023-03-21 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransportMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Марка транспорта',
                'verbose_name_plural': 'Марки транспорта',
            },
        ),
        migrations.CreateModel(
            name='TransportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Модель')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.transportmark', verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Модель транспорта',
                'verbose_name_plural': 'Модели транспорта',
            },
        ),
        migrations.CreateModel(
            name='TransportAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_transport', models.CharField(choices=[('авто', 'Авто')], max_length=32, verbose_name='Тип транспорта')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('price_in_dollar', models.IntegerField(verbose_name='Цена')),
                ('engine', models.CharField(choices=[('бензин', 'Бензин'), ('бензин(пропан-бутан)', 'Бензин(пропан-бутан)'), ('бензин(метан)', 'Бензин(метан)'), ('бензин(гибрид)', 'Бензин(гибрид)'), ('дизель', 'Дизель'), ('дизель(гибрид)', 'Дизель(гибрид'), ('электро', 'Электро')], max_length=32, verbose_name='Двигатель')),
                ('engine_capacity', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Объем двигателя')),
                ('drive_unit', models.CharField(choices=[('передний привод', 'Передний привод'), ('задний привод', 'Задний привод'), ('постоянный полный привод', 'Постоянный полный привод'), ('подключаемый полный привод', 'Подключаемый полный привод')], max_length=32, verbose_name='Привод')),
                ('mileage', models.IntegerField(verbose_name='Пробег')),
                ('vin_number', models.CharField(blank=True, max_length=17, null=True, verbose_name='ВИН номер')),
                ('status', models.CharField(choices=[('открыто', 'Открыто'), ('Закрыто', 'Закрыто')], max_length=16, verbose_name='Статус')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('post_date', models.DateTimeField(auto_now=True, verbose_name='Дата подачи')),
                ('close_date', models.DateTimeField(verbose_name='Дата снятия')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='back.transportmark', verbose_name='Марка')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='back.transportmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
