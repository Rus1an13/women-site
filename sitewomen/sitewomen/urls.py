from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import settings
from women import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path('users/', include('users.urls', namespace="users")),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = views.page_not_found

# handler500 = views.server_error

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщины мира"
