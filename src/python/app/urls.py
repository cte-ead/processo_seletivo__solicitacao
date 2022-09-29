from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = 'Solicitação de processo seletivo'
admin.site.site_header = admin.site.site_title

urlpatterns = [
    path('admin/login/', RedirectView.as_view(url='/login/')),
    path('admin/', admin.site.urls),
    path('health/', include('health.urls')),
    path('', include('processoseletivo.urls')),
    path('', include('a4.urls')),
    path('', RedirectView.as_view(url='/admin/'), name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('/__debug__/', include(debug_toolbar.urls)))
