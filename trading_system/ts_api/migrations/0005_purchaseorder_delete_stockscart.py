# Generated by Django 4.0.6 on 2022-07-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts_api', '0004_alter_stockscart_cart_id_alter_stocksitem_stock_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('cart_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('stock_name', models.CharField(max_length=50)),
                ('stock_price', models.FloatField()),
                ('stock_quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='StocksCart',
        ),
    ]
