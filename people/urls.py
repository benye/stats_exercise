from django.conf.urls import patterns, include, url
from things import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'people.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^list/$',views.display_stuff,name = 'display_things'),
    #url(r'^/$',views.display_stuff,name = 'display_things'),
)
