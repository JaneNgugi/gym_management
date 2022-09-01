from django.contrib import admin
from .models import Health,WeightCat,BmiChart
# Register your models here.
class BmiAdmin(admin.ModelAdmin):
    
    list_display=("bmi","weight_category","health_Risk")

# Register your models here.
admin.site.register(BmiChart, BmiAdmin)
admin.site.register(WeightCat)
admin.site.register(Health)
