# Generated by Django 4.0.5 on 2022-06-22 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_time_remove_item_updatedate_item_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='parentId',
        ),
        migrations.AddField(
            model_name='item',
            name='parent',
            field=models.ForeignKey(db_column='parentId', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.item'),
        ),
    ]
