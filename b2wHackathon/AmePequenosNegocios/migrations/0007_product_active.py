# Generated by Django 3.1 on 2020-08-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmePequenosNegocios', '0006_auto_20200822_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]