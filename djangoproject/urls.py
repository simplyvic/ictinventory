from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'djangoapp.views.home', name='home'),
    url(r'^computer_entry/$', 'djangoapp.views.computer_entry', name='computer_entry'),
    url(r'^computer_list/$', 'djangoapp.views.computer_list', name='computer_list'),
    url(r'^settings/$', 'djangoapp.views.settings', name='settings'),
    url(r'^computer_audit/$', 'djangoapp.views.computer_audit', name='computer_audit'),

    url(r'^computer_list/(?P<id>\d+)/delete$', 'djangoapp.views.computer_delete', name='computer_delete'),
    url(r'^computer_list/(?P<id>\d+)/edit$', 'djangoapp.views.computer_edit', name='computer_edit'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
