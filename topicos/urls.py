from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'topicos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dante/', include(admin.site.urls)),
    url(r'^app/', include('apps.estadia.urls', namespace='u-app')),
    url(r'^app/busqueda/', include('apps.busqueda.urls', namespace='u-app-busqueda')),


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
