from django.contrib import admin
from .models import Item

# Register your models here.
@admin.register(Item)
class UserAdmin(admin.ModelAdmin):
     list_display = ['name', 'description', 'price'] 
     search_fields = ['name']