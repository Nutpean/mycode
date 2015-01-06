from django.contrib import admin

# Register your models here.
from workstation.models import HelpdeskDeliver

class DeliverAdmin( admin.ModelAdmin ):
    list_display = ( 'casenum', 'casetitle', 'creator', 'engineer', 'description', 'emergency', 'duty', 'dates', 'schedule', 'alive' )

admin.site.register( HelpdeskDeliver, DeliverAdmin )
