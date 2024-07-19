from django.contrib import admin
from core_apps.profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "gender", "phone_number"]
    list_display_links = ["pkid","id","user"]
    list_filter = ["pkid","id"]


admin.site.register(Profile, ProfileAdmin)