# Generated by Django 3.2.4 on 2021-06-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('Double Double', 'Double Double'), ('Quad', 'Quad'), ('4 Person', '4 Person'), ('Double', 'Double'), ('Twin', 'Twin'), ('Dorm', 'Dorm')], default='Double', max_length=20)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=400)),
                ('no_of_roommates', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=20)),
                ('price', models.SmallIntegerField()),
                ('rental_period', models.DurationField()),
                ('photo', models.ImageField(height_field=100, upload_to='uploads/', width_field=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
