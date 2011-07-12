from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    (r'^frats/$', 'frats.views.index'),
    (r'^frats/(?P<frat_id>\d+)/$', 'frats.views.detail'),
<<<<<<< HEAD
=======
    url(r'^admin/', include(admin.site.urls)),
>>>>>>> c199b9df9b29327c52c1b92a2efa3c575b4e0c5a
)
