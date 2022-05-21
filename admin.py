from django.contrib import admin
from .models import models_list

# Register your models here.

for model in models_list:
    admin.site.register(model)