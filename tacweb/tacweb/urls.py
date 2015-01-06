from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('tacwebapp.views',
    # Examples:
    # url(r'^$', 'tacweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^update/', 'update_action'),
    #url(r'^onoff/', 'onoff_action'),
    #url(r'^manage/', 'manage'),
    url(r'^list/$', 'listing'),
    url(r'^show/$', 'webpage'),
    url(r'^upda/', 'update'),
)
