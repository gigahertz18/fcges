# Generated by Django 4.0.6 on 2022-07-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts_api', '0003_rename_stock_unit_stockscart_stock_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockscart',
            name='cart_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stocksitem',
            name='stock_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]