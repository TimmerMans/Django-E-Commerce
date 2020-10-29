# Generated by Django 3.1.2 on 2020-10-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Финальная цена'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='full_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена'),
        ),
        migrations.AlterField(
            model_name='notebookproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='smartphoneproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена'),
        ),
    ]