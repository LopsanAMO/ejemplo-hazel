from django.conf.urls import url, include
from django.contrib import admin
from proyecto import urls as zeldas

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^proyecto/', include(zeldas , namespace="proyectolo"))
]
