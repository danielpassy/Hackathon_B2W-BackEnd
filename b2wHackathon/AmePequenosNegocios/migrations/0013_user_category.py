# Generated by Django 3.1 on 2020-08-24 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmePequenosNegocios', '0012_auto_20200823_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(default='no', max_length=100),
            preserve_default=False,
        ),
    ]