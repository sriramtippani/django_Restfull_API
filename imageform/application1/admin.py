from django.contrib import admin
from application1.models import Hotel

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'document', 'uploaded_at']

admin.site.register(Hotel, HotelAdmin)