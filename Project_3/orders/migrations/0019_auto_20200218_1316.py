# Generated by Django 2.2.10 on 2020-02-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200217_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='tops',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=0),
        ),
    ]
