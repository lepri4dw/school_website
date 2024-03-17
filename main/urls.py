from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main.views import about_view

urlpatterns = [
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
    path('teachers/', include('teachers.urls')),
    path('', include('applications.urls')),
    path('', include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
