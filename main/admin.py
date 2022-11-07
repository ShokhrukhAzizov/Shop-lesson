from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('company',)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Comment)
# admin.site.register(User)