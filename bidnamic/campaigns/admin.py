from django.contrib import admin

from bidnamic.campaigns.models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ["id", "structure_value", "status"]
