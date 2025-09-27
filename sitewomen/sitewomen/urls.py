from django.contrib import admin
from django.urls import path, include
from women import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

# handler404 = views.page_not_found

# handler500 = views.server_error

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщины мира"
