from django.contrib import admin

# Register your models here.
from .models import Semester
from .models import UserProfile
from .models import Position

admin.site.register(Semester)
admin.site.register(UserProfile)
admin.site.register(Position)
