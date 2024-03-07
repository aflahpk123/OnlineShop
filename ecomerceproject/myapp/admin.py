from django.contrib import admin

# Register your models here.
from . models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','desc','img']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created',]
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 30
admin.site.register(Product,ProductAdmin)