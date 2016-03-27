from django.contrib import admin

# Register your models here.
from .models import Portfolio, Asset, Security, User

admin.site.register(Portfolio)
admin.site.register(Asset)
admin.site.register(Security)
admin.site.register(User)
