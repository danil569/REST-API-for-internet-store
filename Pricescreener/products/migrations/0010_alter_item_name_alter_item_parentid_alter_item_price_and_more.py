# Generated by Django 4.0.5 on 2022-06-29 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_time_item_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='parentId',
            field=models.ForeignKey(db_column='parentId', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='updateDate',
            field=models.DateTimeField(),
        ),
    ]
