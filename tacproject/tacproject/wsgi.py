"""
WSGI config for tacproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

#import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tacproject.settings")

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()


import os
import sys
import django.core.handlers.wsgi
sys.path.append(r'/home/peanut/gdjcode/tacproject/tacproject')
#sys.path.append(r'E:/Project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tacproject.settings'
application = django.core.handlers.wsgi.WSGIHandler()
