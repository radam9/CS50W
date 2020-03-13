# Generated by Django 2.2.10 on 2020-02-06 16:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Subs', 'Subs'), ('Salads', 'Salads'), ('Pasta', 'Pasta'), ('Dinner Pallates', 'Dinner Pallates')], max_length=16),
        ),
    ]
