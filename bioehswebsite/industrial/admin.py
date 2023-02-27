from django.contrib import admin
# Register your models here.

from .models import Sponsor, Year


admin.site.register(Sponsor)
admin.site.register(Year)

