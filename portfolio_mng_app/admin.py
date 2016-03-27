from django.contrib import admin

# Register your models here.
from .models import Portfolio, Security, User

admin.site.register(Portfolio)
admin.site.register(Security)
admin.site.register(User)
