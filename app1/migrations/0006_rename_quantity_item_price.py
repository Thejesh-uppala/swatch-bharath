# Generated by Django 4.0.4 on 2022-06-01 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_item_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Quantity',
            new_name='Price',
        ),
    ]