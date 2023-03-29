# Generated by Django 4.1.7 on 2023-03-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_alter_transportad_close_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportad',
            name='body',
            field=models.CharField(choices=[('all_road_3d', 'внедорожник 3 дв.'), ('all_road_5d', 'внедорожник 5 дв.'), ('cabriolet', 'кабриолет'), ('coupe', 'купе'), ('light_van', 'легковой фургон'), ('limousine', 'лимузин'), ('lift_back', 'лифтбек'), ('minivan', 'минивэн'), ('pickup', 'пикап'), ('sedan', 'седан'), ('station_wagon', 'универсал'), ('hatchback_3d', 'хэтчбек 3 дв.'), ('hatchback_5d', 'хэтчбек 5 дв.'), ('other', 'другой')], max_length=32, null=True, verbose_name='Кузов'),
        ),
        migrations.AddField(
            model_name='transportad',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'автоматическая'), ('mechanical', 'механическая')], max_length=32, null=True, verbose_name='трансмиссия'),
        ),
        migrations.AlterField(
            model_name='transportad',
            name='drive_unit',
            field=models.CharField(choices=[('front_drive', 'Передний привод'), ('back_drive', 'Задний привод'), ('constant_full_drive', 'Постоянный полный привод'), ('plug_in_full_drive', 'Подключаемый полный привод')], max_length=32, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='transportad',
            name='engine',
            field=models.CharField(choices=[('petrol', 'Бензин'), ('propane_butane', 'Бензин(пропан-бутан)'), ('methane', 'Бензин(метан)'), ('hybrid', 'Бензин(гибрид)'), ('diesel', 'Дизель'), ('diesel_hybrid', 'Дизель(гибрид'), ('electro', 'Электро')], max_length=32, verbose_name='Двигатель'),
        ),
        migrations.AlterField(
            model_name='transportad',
            name='status',
            field=models.CharField(choices=[('open', 'Открыто'), ('close', 'Закрыто')], default='open', max_length=16, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='transportad',
            name='type_of_transport',
            field=models.CharField(choices=[('auto', 'Авто')], max_length=32, verbose_name='Тип транспорта'),
        ),
    ]