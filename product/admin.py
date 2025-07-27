from django.contrib import admin
from .models import Estate, Category, City, District, Image


class EstateAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'state', 'city', 'district')
    list_filter = ('category', 'city', 'district')
    search_fields = ('title', 'state', 'city', 'district')


admin.site.register(Estate)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Image)