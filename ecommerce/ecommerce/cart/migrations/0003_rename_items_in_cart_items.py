# Generated by Django 4.0.5 on 2022-06-30 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0001_initial'),
        ('cart', '0002_items_in_cart_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items_in_cart',
            new_name='items',
        ),
    ]
