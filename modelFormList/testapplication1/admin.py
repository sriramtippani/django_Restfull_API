from django.contrib import admin
from testapplication1.models import modelForm1
# Register your models here.
class AdminForm(admin.ModelAdmin):
    list_display = ['name', 'number']
admin.site.register(modelForm1, AdminForm)