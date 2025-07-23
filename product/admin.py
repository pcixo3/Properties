from django.contrib import admin
from .models import Product, Category, City, District

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(District)
