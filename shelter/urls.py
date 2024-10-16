from django.urls import path

from shelter.apps import ShelterConfig
from shelter.views import cat_list, cat_detail, shelter_detail, help_detail

app_name = ShelterConfig.name

urlpatterns = [
    path('', cat_list, name='cat_list'),
    path('cat/<int:pk>/', cat_detail, name='cat_detail'),
    path('shelter/', shelter_detail, name='shelter_detail'),
    path('help/', help_detail, name='help_detail'),

]
