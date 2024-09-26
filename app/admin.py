from django.contrib import admin
from app.models import Admin



@admin.register(Admin)
class AdminModel(admin.ModelAdmin):
    list_display = ('name', 'email', )

