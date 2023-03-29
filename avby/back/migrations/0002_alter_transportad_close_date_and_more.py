# Generated by Django 4.1.7 on 2023-03-25 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportad',
            name='close_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата снятия'),
        ),
        migrations.AlterField(
            model_name='transportad',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='transportad',
            name='status',
            field=models.CharField(choices=[('открыто', 'Открыто'), ('Закрыто', 'Закрыто')], default='открыто', max_length=16, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('transport_ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.transportad', verbose_name='Объявление')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
