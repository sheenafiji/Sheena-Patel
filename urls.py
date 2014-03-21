from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/$', 'webpage.views.home', name='home'),
    url(r'^aboutme/$', 'webpage.views.aboutme', name='aboutme'),
    url(r'^resume/$', 'webpage.views.resume', name='resume'),
    url(r'^travels/$', 'webpage.views.travels', name='travels'),
    url(r'^contact/$', 'webpage.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
