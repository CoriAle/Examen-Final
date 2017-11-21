from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^grado/nuevo/$', views.grado_nuevo, name='grado_nuevo'),
    url(r'^grado/listar/$', views.grado_list, name='grado_list'),
]
