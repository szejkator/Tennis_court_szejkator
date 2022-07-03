# Generated by Django 4.0.5 on 2022-07-03 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0006_alter_reservations_client_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
