from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(section)


class partyAdmin(admin.ModelAdmin):
    # Columns to display in the table (like in the User table)
    list_display = ('section', 'npp_votes', 'ndc_votes', 'mp_npp', 'mp_ndc', 'created_at')

    list_editable = ('npp_votes', 'ndc_votes', 'mp_npp', 'mp_ndc')

    # Optional: Allow filtering of the table by certain fields
    list_filter = ('created_at',)

    # Optional: Add a search bar that searches specific fields
    # search_fields = ('name', 'votes', 'group')
    search_fields = ('section__name', 'npp_votes')


# Register the model with the admin site
admin.site.register(Vote, partyAdmin)
