from django.urls import path
from .views import *


urlpatterns = [
    path('Recipes/random', recipes_random),
    path('Recipes/', recipes_all),
    path('Recipe/<str:pk>/', recipe_info),
    path('Client/<str:pk>/', client_info),
    path('Recipes_by_title/<str:search_title>/', recipes_by_title),
    path('Recipes_by_tag/<str:search_tag>/', recipes_by_tag),
    path('Recipes_by_author/<str:search_author>/', recipes_by_author),
]
