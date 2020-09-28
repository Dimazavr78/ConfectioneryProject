from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *
# from django.conf import settings


##### Сериализаторы данных пользователя #####

# (к примеру, для карточки рецепта)
class ClientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'username')


# (к примеру, для страницы рецепта)
class ClientSurfaceSerializer(ClientSimpleSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta(ClientSimpleSerializer.Meta):
        fields = ClientSimpleSerializer.Meta.fields + ('avatar',)

    def get_avatar(self, client_obj):
        # settings.BASE_DIR + client.avatar.url
        return client_obj.avatar.url


# (к примеру, для публичной части страницы пользователя)
class ClientShowSerializer(ClientSurfaceSerializer):
    status = serializers.SerializerMethodField()

    class Meta(ClientSurfaceSerializer.Meta):
        fields = ClientSurfaceSerializer.Meta.fields + ('first_name', 'last_name', 'patronymic', 'status',
                                                        'date_joined', 'last_login')

    def get_status(self, client_obj):
        if client_obj.is_active:
            return "Активен"
        else:
            return "Заблокирован"


# (к примеру, для страницы пользователя)
class ClientSerializer(ClientSurfaceSerializer):
    class Meta(ClientSurfaceSerializer.Meta):
        fields = ClientSurfaceSerializer.Meta.fields + ('first_name', 'last_name', 'patronymic', 'email')



##### Сериализаторы данных тега #####

# (к примеру, для страницы рецепта)
class TagSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedTag
        fields = ('id', 'name')



##### Сериализаторы данных комментария #####

# (к примеру, для страницы рецепта)
class CommentSerializer(serializers.ModelSerializer):
    creator = ClientShowSerializer()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'creator', 'body', 'date_init', 'rating')

    def get_rating(self, comment_obj):
        grades = CommentGrade.objects.filter(comment=comment_obj.pk)
        rating_value = 0
        # Проходимся по всем объектам оценивания и подсчитываем общий рейтинг
        for grade in grades:
            if grade.grade:
                rating_value += 1
            else:
                rating_value -= 1
        return rating_value



##### Сериализаторы данных прикреплённого изображения #####

class FixedPictureSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = FixedPicture
        fields = ('id', 'picture',)

    def get_picture(self, picture_obj):
        return picture_obj.picture.url



##### Сериализаторы данных рецепта #####

# (к примеру, для карточки рецепта)
class RecipeShowSerializer(serializers.ModelSerializer):

    creator = ClientSimpleSerializer()
    avatar = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('id', 'creator', 'title', 'avatar', 'rating')

    def get_rating(self, recipe_obj):
        grades = RecipeGrade.objects.filter(recipe=recipe_obj.pk)
        rating_value = 0
        # Проходимся по всем объектам оценивания и подсчитываем общий рейтинг
        for grade in grades:
            if grade.grade:
                rating_value += 1
            else:
                rating_value -= 1
        return rating_value

    def get_avatar(self, recipe_obj):
        return recipe_obj.avatar.url


# (к примеру, для страницы рецепта)
class RecipeSerializer(RecipeShowSerializer):

    creator = ClientSurfaceSerializer()
    fixed_pictures = FixedPictureSerializer(many=True)
    fixed_tags = TagSimpleSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta(RecipeShowSerializer.Meta):
        fields = RecipeShowSerializer.Meta.fields + ('body', 'date_init', 'fixed_pictures', 'fixed_tags', 'comments')
