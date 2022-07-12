from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('import/', ImportView.as_view()),
    path('nodes/', NodesView.as_view()),
    path('nodes/<uuid:pk>', NodesIdView.as_view()),
    path('delete/<uuid:pk>', DeleteIdView.as_view()),
]