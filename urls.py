from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from django.conf import settings
from frats.models import *
from unis.models import *
<<<<<<< HEAD

=======
>>>>>>> c199b9df9b29327c52c1b92a2efa3c575b4e0c5a
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

<<<<<<< HEAD

=======
>>>>>>> c199b9df9b29327c52c1b92a2efa3c575b4e0c5a
urlpatterns = patterns('',
    # Examples:
	url(r'^$', ListView.as_view(queryset=University.objects.order_by('-name'),context_object_name='uni_list',template_name='home/index.html')),
)

urlpatterns += patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<university_name>\w+)/$', include('frats.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

<<<<<<< HEAD
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
=======
>>>>>>> c199b9df9b29327c52c1b92a2efa3c575b4e0c5a


INTERNAL_IPS = ('127.0.0.1',)
