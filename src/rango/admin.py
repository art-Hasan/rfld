from django.contrib import admin
from rango.models import Category, Page

class PageInline(admin.StackedInline):
    model = Page
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [PageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
