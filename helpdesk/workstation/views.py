from django.shortcuts import render_to_response

# Create your views here.

from workstation.models import *

def hello( request ):
    deliver = HelpdeskDeliver.objects.order_by('casenum')
    return render_to_response( 'base.html', {'deliver':deliver} )
