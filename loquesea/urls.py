from django.conf.urls import url, include
from django.contrib import admin
from proyecto import urls as zeldas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^proyecto/', include(zeldas , namespace="proyectolo"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
