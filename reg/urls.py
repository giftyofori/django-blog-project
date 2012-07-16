from django.conf.urls.defaults import *

urlpatterns = patterns('',
   
    url(r'^login/$', 'reg.views.do_login'),
    url(r'reg/logout/$','reg.views.do_logout'),
)
