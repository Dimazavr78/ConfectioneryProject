'''
from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth import admin as auth_admin


class ClientAdmin(admin.ModelAdmin):
    form = ClientChangeForm
    add_form = ClientCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'patronymic')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('creator', 'title', 'body', 'avatar', 'status', 'date_init')


class FixedPictureAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'picture')


class FixedTagAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'tag')


class RecipeGradeAdmin(admin.ModelAdmin):
    list_display = ('evaluator', 'recipe', 'grade')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('creator', 'recipe', 'body', 'status', 'date_init')


class CommentGradeAdmin(admin.ModelAdmin):
    list_display = ('evaluator', 'comment', 'grade')


admin.site.register(Client, ClientAdmin)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(FixedPicture, FixedPictureAdmin)
admin.site.register(FixedTag, FixedTagAdmin)
admin.site.register(RecipeGrade, RecipeGradeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentGrade, CommentGradeAdmin)
'''