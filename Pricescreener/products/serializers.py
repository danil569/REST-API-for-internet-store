from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Item, Time
from rest_framework import status
from django.db.models import Avg


class FilterReviewSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ItemListSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    date = serializers.SlugRelatedField(slug_field="updateDate", read_only=True)
    parentId = serializers.SlugRelatedField(slug_field="id", read_only=True)


    class Meta:
        model = Item
        fields = ("type", "name", "id", "price", "parentId", "date", "children")


class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class ImportSerializer(serializers.ModelSerializer):
    items = ItemCreateSerializer(many=True)

    class Meta:
        model = Time
        fields = ['items', 'updateDate']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        date = Time.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.update_or_create(
                id=item_data.get('id', None),
                defaults={
                    'date': date,
                    'name': item_data.get('name'),
                    'parentId': item_data.get('parentId'),
                    'price': item_data.get('price'),
                }
            )
            stop = item_data.get('id')
            while stop:
                element = Item.objects.get(id=stop)
                element.price = Item.objects.filter(parentId=stop).aggregate(Avg('price'))
                stop = element.parentId


    # def update(self, instance, validated_data):
    #     items_data = validated_data.pop('items')
    #     date = Time.objects.create(**validated_data)
            # if item_data.get('type') is "OFFER":
            #     parent_item = Item.objects.get(name='Телевизоры')
            #     parent_item['price'] = 100
        return date

    # def update(self, instance, validated_data):
    #     items_data = validated_data.pop('items')
    #     items = instance.items
    #
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #
    #     items.is_premium_member = items_data.get(
    #         'is_premium_member',
    #         items.is_premium_member
    #     )
    #     items.has_support_contract = items_data.get(
    #         'has_support_contract',
    #         items.has_support_contract
    #     )
    #     items.save()
    #
    #     return instance


