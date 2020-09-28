from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import *
import random


@api_view(['GET'])
@permission_classes([AllowAny])
def recipes_all(request):
    try:
        recipes = Recipe.objects.filter(status='A')
    except Recipe.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeShowSerializer(recipes, many=True)
    return Response({'recipes': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def recipes_random(request):
    quantity = 15
    max_quantity = Recipe.objects.filter(status='A').count()
    if quantity > max_quantity:
        recipes = Recipe.objects.all()
    else:
        # Массив случайных id
        random_id = [0] * quantity
        exist_flg = False
        for i in range(len(random_id)):
            while True:
                random_id[i] = random.randint(1, Recipe.objects.last().pk)
                print(random_id[i])
                if Recipe.objects.filter(status='A', id=random_id[i]).exists():
                    exist_flg = False
                    for j in range(len(random_id)):
                        if random_id[j] == random_id[i] and not i == j:
                            exist_flg = True
                            break
                    if exist_flg:
                        continue
                    else:
                        break
                else:
                    continue
        recipes = Recipe.objects.filter(id__in=random_id)

    serializer = RecipeShowSerializer(recipes, many=True)
    return Response({'recipes': serializer.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def recipes_by_title(request, search_title):
    try:
        recipes = Recipe.objects.filter(status='A', title__icontains=search_title)
    except Recipe.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeShowSerializer(recipes, many=True)
    return Response({'recipes': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def recipes_by_tag(request, search_tag):
    try:
        recipes = Recipe.objects.filter(status='A', fixed_tags__in=(
            FixedTag.objects.filter(name__icontains=search_tag)
        ))
    except Recipe.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeShowSerializer(recipes, many=True)
    return Response({'recipes': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def recipes_by_author(request, search_author):
    try:
        recipes = Recipe.objects.filter(status='A', creator__in=(
            Client.objects.filter(username__icontains=search_author)
        ))
    except Recipe.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeShowSerializer(recipes, many=True)
    return Response({'recipes': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def recipe_info(request, pk):
    try:
        recipe = Recipe.objects.get(id=pk)
    except Recipe.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeSerializer(recipe)
    return Response({'recipe': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def client_info(request, pk):
    try:
        client = Client.objects.get(id=pk)
    except Client.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)
    serializer = ClientShowSerializer(client)
    return Response({'client': serializer.data}, status=status.HTTP_200_OK)
