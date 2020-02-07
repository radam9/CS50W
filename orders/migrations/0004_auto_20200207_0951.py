# Generated by Django 2.2.10 on 2020-02-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200206_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='category',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Subs', 'Subs'), ('Steak+Cheese', 'Steak+Cheese')], default='Pizza', max_length=20),
        ),
        migrations.AddField(
            model_name='topping',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order Received', 'Order Received'), ('Processing', 'Processing'), ('On Route', 'On Route'), ('Delivered', 'Delivered')], max_length=20),
        ),
    ]
