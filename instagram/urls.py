from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
# to allow serving media files during developement
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return HttpResponse('Instagram WebSite Work')

urlpatterns = [
    path('', index),
    path('accounts/', include('accounts.urls')),
    path('albums/', include('albums.urls', namespace='albums')),
    path('admin/', admin.site.urls),
]

# serving media files only during developement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
