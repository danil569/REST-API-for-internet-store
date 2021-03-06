# Generated by Django 4.0.5 on 2022-06-22 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_item_parentid_item_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='parent',
            field=models.ForeignKey(db_column='parent', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.item'),
        ),
    ]
