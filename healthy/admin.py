from django.contrib import admin
from .models import UserProfile, Lab, Item

admin.site.register(UserProfile)
admin.site.register(Lab)
admin.site.register(Item)
