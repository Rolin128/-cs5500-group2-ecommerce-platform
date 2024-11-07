from django.contrib import admin

# Register your models here.

from . models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}





