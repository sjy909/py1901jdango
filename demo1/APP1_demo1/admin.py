from django.contrib import admin

# Register your models here.
from .models import Book_list, Roles_list


# 关联注册
class Roles_listInline(admin.StackedInline):
    model = Book_list
    extra = 1


# 显示
class Book_listAdmin(admin.ModelAdmin):
    list_display = ['bookName', 'BookPublishDate']


class Roles_listAdmin(admin.ModelAdmin):
    list_display = ['role_name', 'Roles_gerden']
    list_filter = ['role_name']
    search_fields = ['role_name']


admin.site.register(Book_list, Book_listAdmin)
admin.site.register(Roles_list, Roles_listAdmin)
