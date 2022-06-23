# Generated by Django 4.0.5 on 2022-06-23 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TennisCourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('open_hour', models.TimeField()),
                ('hire_price', models.IntegerField()),
                ('close_hour', models.TimeField()),
                ('city', models.CharField(choices=[('Kraków', 'Kraków'), ('Poznań', 'Poznań'), ('Warszawa', 'Warszawa'), ('Olsztyn', 'Olsztyn'), ('Wrocław', 'Wrocaław')], max_length=24)),
                ('adress', models.CharField(max_length=128)),
                ('equipment_rent', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_start', models.TimeField()),
                ('reservation_end', models.TimeField()),
                ('reservation_date', models.DateTimeField(auto_now_add=True)),
                ('reservation_status', models.BooleanField(default=False)),
                ('reservation_cost', models.IntegerField()),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservations.tenniscourt')),
            ],
        ),
    ]
