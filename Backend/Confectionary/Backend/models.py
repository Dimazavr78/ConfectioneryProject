from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    patronymic = models.CharField(max_length=80, blank=True, verbose_name='Отчество')
    avatar = models.ImageField(upload_to=settings.MEDIA_DIR + '/ClientAvatars', blank=True,
                               default=settings.MEDIA_DIR + 'client_default.jpg', verbose_name='Аватарка')


class Recipe(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='recipes',
                                verbose_name='Рецепт')
    title = models.CharField(max_length=100, default='', verbose_name='Наименование')
    body = models.TextField(default='', verbose_name='Описание')
    avatar = models.ImageField(upload_to=settings.MEDIA_DIR + '/RecipeAvatars', blank=True,
                               default=settings.MEDIA_DIR + 'recipe_default.jpg', verbose_name='Аватарка')
    status_vars = (
        ('A', 'В широком доступе'),
        ('B', 'Заблокировано'),
    )
    status = models.CharField(max_length=3, choices=status_vars, default='A', verbose_name='Статус')
    date_init = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class FixedPicture(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='fixed_pictures',
                               verbose_name='Рецепт')
    picture = models.ImageField(upload_to=settings.MEDIA_DIR + '/RecipePictures', blank=True,
                                default=settings.MEDIA_DIR + 'picture_default.jpg', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Прикреплённое изображение'
        verbose_name_plural = 'Прикреплённые изображения'
        unique_together = ('recipe', 'picture')


class FixedTag(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='fixed_tags', verbose_name='Рецепт')
    name = models.CharField(max_length=30, default='', unique=True, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Прикреплённый тег'
        verbose_name_plural = 'Прикреплённые теги'


class RecipeGrade(models.Model):
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipe_grades',
                                  verbose_name='Оценивающий')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_grades', verbose_name='Рецепт')
    grade = models.BooleanField(default=True, verbose_name='Оценка')

    class Meta:
        verbose_name = 'Оценка рецепта'
        verbose_name_plural = 'Оценки рецептов'
        unique_together = ('evaluator', 'recipe')


class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='comments',
                                verbose_name='Создатель')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments', verbose_name='Рецепт')
    body = models.TextField(default='', verbose_name='Содержание')
    status_vars = (
        ('A', 'В широком доступе'),
        ('B', 'Заблокировано'),
    )
    status = models.CharField(max_length=3, choices=status_vars, default='A', verbose_name='Статус')
    date_init = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class CommentGrade(models.Model):
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_grades',
                                  verbose_name='Оценивающий')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_grades',
                                verbose_name='Комментарий')
    grade = models.BooleanField(default=True, verbose_name='Оценка')

    class Meta:
        verbose_name = 'Оценка комментария'
        verbose_name_plural = 'Оценки комментариев'
        unique_together = ('evaluator', 'comment')