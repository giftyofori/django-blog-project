from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'G_blog.views.home', name='home'),
    # url(r'^admin/', include(admin.sites.urls)),
    # url(r'^G_blog/', include('G_blog.foo.urls')),
    url(r'^reg/',include('reg.urls')),
    url(r'^blog/',include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
