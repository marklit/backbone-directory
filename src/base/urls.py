from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r"^api/", include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls')),
    url(r'^$', include('home.urls')),
)

if settings.DEBUG:
    for folder_name in ('css', 'js', 'img', 'lib', 'tpl'):
        urlpatterns += patterns('',
            url(r'^%s/(?P<path>.*)$' % folder_name, 
                'django.views.static.serve', {
                    'document_root': "../frontend/%s/" % folder_name,
                }
            )
        )