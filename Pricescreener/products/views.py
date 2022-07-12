from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import Item, Time


class ImportView(APIView):

    class Meta:
        model = Time
        fields ='__all__'

    def post(self, request):
        serializer = ImportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Вставка или обновление прошли успешно."}, status=200)
        else:
            # return Response({"Невалидная схема документа или входные данные не верны."}, status=400)
            return Response(serializer.errors, status=400)


class NodesView(APIView):

    def get(self, request):
        items = Item.objects.filter(parentId=None)
        serializer = ItemListSerializer(items, many=True)
        return Response(serializer.data)


class NodesIdView(APIView):

    def get(self, request, pk):
        item = Item.objects.get(id=pk)
        if not item:
            return Response({"error": "Item not found"}, status=404)
        serializer = ItemListSerializer(item)
        return Response(serializer.data)


class DeleteIdView(APIView):

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"Невалидная схема документа или входные данные не верны."}, status=400)
        Item.objects.get(id=pk).delete()
        return Response({"Удаление прошло успешно"}, status=200)

