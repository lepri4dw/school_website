from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main.views import index_view, about_view

urlpatterns = [
    path('', index_view, name='home'),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls),
    path('teachers/', include('teachers.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL)
