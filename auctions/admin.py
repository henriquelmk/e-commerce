from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Bid, Comment

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Bid)
admin.site.register(Comment)