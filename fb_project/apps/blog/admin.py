from django.contrib import admin
from .models import Food,Comment,Post,Category
# Register your models here.
@admin.register(Food)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'food_name',
        'photo',
        'description',
        'category',

    ]


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'food',
        'text',
        'created',
        'updated',

    ]


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'slug',
        'icon',
    ]


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'title',
        'text',
        'created',
        'updated',
        'photo',
        'is_draft',
        'category',
    ]
