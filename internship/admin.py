from django.contrib import admin
from .models import *


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'href', 'time', 'get_products')

    def get_products(self, obj):
        return "\n".join([p.name for p in obj.product_id.all()])

    get_products.short_description = 'Product Name'


class ViewingHistoryAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'lesson_id', 'status', 'time')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ViewingHistory, ViewingHistoryAdmin)
