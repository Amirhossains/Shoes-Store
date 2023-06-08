from django.contrib import admin

from .models import CommentModel, ShoesModel

class InlineCommentsAdmin(admin.TabularInline):
    model = CommentModel
    fields = ['shoes', 'title', 'text', 'like']
    extra = 0

@admin.register(ShoesModel)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'mark', 'size', 'isAvailable', 'price', 'createdTime']
    list_filter = ['isAvailable', 'gender']
    inlines = [InlineCommentsAdmin]

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'shoes', 'title', 'like', 'createdTime']
    list_filter = ['like']
