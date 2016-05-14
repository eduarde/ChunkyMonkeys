from django.contrib import admin
from .models import UserProfile, Lab, Item, LabResults

admin.site.register(UserProfile)
admin.site.register(Lab)
admin.site.register(Item)
admin.site.register(LabResults)
