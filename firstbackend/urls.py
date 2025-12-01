from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def root_view(request):
    """Root endpoint that returns API information"""
    return JsonResponse({
        'message': 'Shreshta Backend API',
        'endpoints': {
            'admin': '/admin/',
            'accounts': '/accounts/',
        },
        'status': 'running'
    })

urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

# Serve media files in both development and production
# (WhiteNoise only handles static files, not media files)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files only in development (DEBUG mode)
# In production, WhiteNoise handles static files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
