# Generated by Django 3.1.3 on 2020-11-19 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0004_auto_20201118_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='idCategory',
            new_name='category',
        ),
    ]