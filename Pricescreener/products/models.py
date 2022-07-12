from django.db import models


class Time(models.Model):
    updateDate = models.DateTimeField()


class Item(models.Model):
    date = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='items', default=None, null=True)
    TYPE_TYPES = (
        ('CATEGORY', 'Категория'),
        ('OFFER', 'Товар'))
    type = models.SlugField(max_length=10, default='CATEGORY', choices=TYPE_TYPES)
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    parentId = models.ForeignKey('self', db_column='parentId', on_delete=models.CASCADE, null=True, related_name='children')
    # parentId = models.UUIDField(db_column='parentId', null=True)
    price = models.IntegerField(null=True)
