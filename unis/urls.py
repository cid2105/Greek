from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    (r'^frats/$', 'frats.views.index'),
    (r'^frats/(?P<frat_id>\d+)/$', 'frats.views.detail'),
)
