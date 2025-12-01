from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

# Serve media files (uploads)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files (CSS, JS, images)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
