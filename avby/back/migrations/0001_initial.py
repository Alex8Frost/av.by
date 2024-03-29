# Generated by Django 4.1.7 on 2023-04-13 20:53

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
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
                ('type_of_transport', models.CharField(choices=[('auto', 'Авто')], max_length=32, verbose_name='Тип транспорта')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('price_in_dollar', models.IntegerField(verbose_name='Цена')),
                ('engine', models.CharField(choices=[('petrol', 'Бензин'), ('propane_butane', 'Бензин(пропан-бутан)'), ('methane', 'Бензин(метан)'), ('hybrid', 'Бензин(гибрид)'), ('diesel', 'Дизель'), ('diesel_hybrid', 'Дизель(гибрид'), ('electro', 'Электро')], max_length=32, verbose_name='Двигатель')),
                ('engine_capacity', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Объем двигателя')),
                ('drive_unit', models.CharField(choices=[('front_drive', 'Передний привод'), ('back_drive', 'Задний привод'), ('constant_full_drive', 'Постоянный полный привод'), ('plug_in_full_drive', 'Подключаемый полный привод')], max_length=32, verbose_name='Привод')),
                ('mileage', models.IntegerField(verbose_name='Пробег')),
                ('vin_number', models.CharField(blank=True, max_length=17, null=True, verbose_name='ВИН номер')),
                ('status', models.CharField(choices=[('open', 'Открыто'), ('close', 'Закрыто')], default='open', max_length=16, verbose_name='Статус')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('post_date', models.DateTimeField(auto_now=True, verbose_name='Дата подачи')),
                ('close_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата снятия')),
                ('body', models.CharField(choices=[('all_road_3d', 'внедорожник 3 дв.'), ('all_road_5d', 'внедорожник 5 дв.'), ('cabriolet', 'кабриолет'), ('coupe', 'купе'), ('light_van', 'легковой фургон'), ('limousine', 'лимузин'), ('lift_back', 'лифтбек'), ('minivan', 'минивэн'), ('pickup', 'пикап'), ('sedan', 'седан'), ('station_wagon', 'универсал'), ('hatchback_3d', 'хэтчбек 3 дв.'), ('hatchback_5d', 'хэтчбек 5 дв.'), ('other', 'другой')], max_length=32, null=True, verbose_name='Кузов')),
                ('transmission', models.CharField(choices=[('automatic', 'автоматическая'), ('mechanical', 'механическая')], max_length=32, null=True, verbose_name='трансмиссия')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='back.transportmark', verbose_name='Марка')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='back.transportmodel', verbose_name='Модель')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
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
