from django.contrib import admin
from .models import goods_list,price_list,comment,Users
# Register your models here.
admin.site.register(goods_list)
admin.site.register(price_list)
admin.site.register(comment)
admin.site.register(Users)