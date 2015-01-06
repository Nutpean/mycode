from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import base64
import time

from models import *
# Create your views here.

#
def show( request ):
    credititem = CreditWebtempnew.objects.filter( event_type='av' )
    for i in credititem:
        i.file_name = base64.decodestring(i.file_name)
        i.referer = base64.decodestring(i.referer)
        i.info0 = base64.decodestring(i.info0)
        i.info1 = base64.decodestring(i.info1)
        i.info2 = base64.decodestring(i.info2)
        i.info3 = base64.decodestring(i.info3)
        i.info4 = base64.decodestring(i.info4)
        i.intern_path = base64.decodestring(i.intern_path)
	i.create_time = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime(i.create_time) )

    return render_to_response( 'showpage.html', {"object_list":credititem} )


#Show alarm items just auto filter, filter_status=1 or filter_status=2
def showlist( request ):
    contact_list = CreditWebtempnew.objects.filter( filter_status__range=(1, 2) )

    for i in contact_list:
        i.file_name = base64.decodestring(i.file_name)
        i.referer = base64.decodestring(i.referer)
        i.info0 = base64.decodestring(i.info0)
        i.info1 = base64.decodestring(i.info1)
        i.info2 = base64.decodestring(i.info2)
        i.info3 = base64.decodestring(i.info3)
        i.info4 = base64.decodestring(i.info4)
        i.intern_path = base64.decodestring(i.intern_path)
	i.create_time = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime(i.create_time) )

    paginator = Paginator(contact_list, 2) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response( 'show.html', {"contacts":contacts} )


#Ajax update function
def update( request ):
    response = HttpResponse()
    temp_id = request.POST.get( "temp_id" )
    filter_status = request.POST.get( "filter_status" )

    update = CreditWebtempnew.objects.get( temp_id=temp_id )
    update.filter_status = filter_status
    update.save()

    return response
