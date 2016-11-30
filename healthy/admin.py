from django.contrib import admin
from .models import UserProfile, Lab, Item, LabResults, LabGeneral, Dictionary

admin.site.register(UserProfile)
admin.site.register(Lab)
admin.site.register(Item)
admin.site.register(LabResults)
admin.site.register(LabGeneral)
admin.site.register(Dictionary)

