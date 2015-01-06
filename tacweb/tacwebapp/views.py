from django.shortcuts import render, HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import subprocess

#from command import *
#from switch import turn_onoff

from models import webtemp
# Create your views here.

#web manage page
def listing( request ):
    alarm = webtemp.objects.all()
    paginator = Paginator( alarm, 1 )
    page = request.GET.get( 'page' )
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response( 'listpage.html', { 'contacts':contacts } )


def webpage( request ):
    alarm = webtemp.objects.order_by( 'status' )
    return render_to_response( 'showpage.html', { 'object_list':alarm } )


def update( request ):
    response = HttpResponse()

    itemid = request.POST.get( "itemid" )
    itemstatus = request.POST.get( "itemstatus" )

    upda = webtemp.objects.get( id=itemid )
    upda.status = itemstatus
    upda.save()

    return response


'''
#
def manage( request ):
    return render_to_response( 'demopage.html' )


#update button view function
def update_action( request ):
    flag = isco_dir()
    if not flag:
        co = checkout_svn()
        co_res = exec_commands( co )
        if co_res != 0:
            return render_to_response( 'demopage.html', {'update_status':'Checkout failed'} )

    up = update_svn()
    up_res = exec_commands( up )
    if up_res == 0:
        return render_to_response( 'demopage.html', {'update_status':'Update successful'} )
    else:
        return render_to_response( 'demopage.html', {'update_status':'Update failed'} )


#turn on off button function
def onoff_action( request ):
    stu = turn_onoff()
    if stu == 1:
        return render_to_response( 'demopage.html', {'switch_status':'Switch ON'} )
    else:
        return render_to_response( 'demopage.html', {'switch_status':'Switch OFF'} )
'''
