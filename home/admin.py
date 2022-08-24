from django.contrib import admin
from . models import catg,prod
# Register your models here.
class catgadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(catg,catgadmin)

class prodadmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(prod,prodadmin)
