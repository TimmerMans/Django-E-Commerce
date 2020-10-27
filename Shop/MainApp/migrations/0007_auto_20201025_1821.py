# Generated by Django 3.1.2 on 2020-10-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_auto_20201025_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphoneproduct',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
        migrations.AlterField(
            model_name='smartphoneproduct',
            name='sd_max_volume',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем SD карты'),
        ),
    ]
