from django.contrib import admin
from .models import *
from .models import Profile

admin.site.register(Company)
admin.site.register(Rate)
admin.site.register(Profile)
# Register your models here.
