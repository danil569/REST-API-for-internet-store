# Generated by Django 4.0.5 on 2022-06-22 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_item_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='parent',
            new_name='parentId',
        ),
    ]
