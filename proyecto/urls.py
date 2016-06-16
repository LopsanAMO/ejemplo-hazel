from django.conf.urls import url
from .views import casita, formi

urlpatterns = [
    url(r'^casi', casita),
    url(r'^formi', formi.as_view())
]
