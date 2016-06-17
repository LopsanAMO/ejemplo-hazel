from django.conf.urls import url, include
from django.contrib import admin
from proyecto import urls as zeldas
<<<<<<< HEAD
from login import urls as urlsLogin
=======
>>>>>>> 09f7e832092b35bafd11940a03f09c3871cf877e
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^proyecto/', include(zeldas , namespace="proyectolo")),
    url(r'^login/', include(urlsLogin, namespace='login'))
=======
    url(r'^proyecto/', include(zeldas , namespace="proyectolo"))
>>>>>>> 09f7e832092b35bafd11940a03f09c3871cf877e
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
