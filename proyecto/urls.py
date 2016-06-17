from django.conf.urls import url
from .views import casita, formi
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^casi', casita),
    url(r'^formi', formi.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
