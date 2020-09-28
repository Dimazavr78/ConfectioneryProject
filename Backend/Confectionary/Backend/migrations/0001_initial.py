# Generated by Django 3.0.3 on 2020-09-27 15:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('patronymic', models.CharField(blank=True, max_length=80, verbose_name='Отчество')),
                ('avatar', models.ImageField(null=True, unique=True, upload_to='C:\\Users\\User\\Desktop\\Git\\Django\\Confectionary\\media/ClientAvatars', verbose_name='Аватарка')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Наименование')),
                ('body', models.TextField(default='', verbose_name='Описание')),
                ('avatar', models.ImageField(blank=True, null=True, unique=True, upload_to='C:\\Users\\User\\Desktop\\Git\\Django\\Confectionary\\media/RecipeAvatars', verbose_name='Аватарка')),
                ('status', models.CharField(choices=[('A', 'В широком доступе'), ('B', 'Заблокировано')], default='A', max_length=3, verbose_name='Статус')),
                ('date_init', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='FixedTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, unique=True, verbose_name='Наименование')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_tags', to='Backend.Recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Прикреплённый тег',
                'verbose_name_plural': 'Прикреплённые теги',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='', verbose_name='Содержание')),
                ('status', models.CharField(choices=[('A', 'В широком доступе'), ('B', 'Заблокировано')], default='A', max_length=3, verbose_name='Статус')),
                ('date_init', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Backend.Recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='RecipeGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.BooleanField(default=True, verbose_name='Оценка')),
                ('evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_grades', to=settings.AUTH_USER_MODEL, verbose_name='Оценивающий')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_grades', to='Backend.Recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Оценка рецепта',
                'verbose_name_plural': 'Оценки рецептов',
                'unique_together': {('evaluator', 'recipe')},
            },
        ),
        migrations.CreateModel(
            name='FixedPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, unique=True, upload_to='C:\\Users\\User\\Desktop\\Git\\Django\\Confectionary\\media/RecipePictures', verbose_name='Изображение')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixed_pictures', to='Backend.Recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Прикреплённое изображение',
                'verbose_name_plural': 'Прикреплённые изображения',
                'unique_together': {('recipe', 'picture')},
            },
        ),
        migrations.CreateModel(
            name='CommentGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.BooleanField(default=True, verbose_name='Оценка')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_grades', to='Backend.Comment', verbose_name='Комментарий')),
                ('evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_grades', to=settings.AUTH_USER_MODEL, verbose_name='Оценивающий')),
            ],
            options={
                'verbose_name': 'Оценка комментария',
                'verbose_name_plural': 'Оценки комментариев',
                'unique_together': {('evaluator', 'comment')},
            },
        ),
    ]
