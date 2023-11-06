from django.contrib import admin
from .models import adde, reserves

# Register your models here.
admin.site.register([adde, reserves])