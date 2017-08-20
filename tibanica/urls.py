from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^socioecologico/$', views.socioecologico, name='socioecologico'),
    url(r'^biodiversidad/$', views.biodiversidad, name='biodiversidad'),
    url(r'^cartografia/$', views.cartografia, name='cartografia'),
    url(r'^biblioteca/$', views.biblioteca, name='biblioteca'),
    url(r'^comic/$', views.comic, name='comic'),
    url(r'^nosotros/$', views.nosotros, name='nosotros'),
    url(r'^paginasamigas/$', views.paginasamigas, name='paginasamigas'),
    url(r'^visitahumedal/$', views.visitahumedal, name='visitahumedal'),
]