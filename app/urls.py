from django.urls import path
from app.views import inicio
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from .views import *

urlpatterns = [
    path('', inicio),
    path('crear/', views.crear_publicacion, name='crear_post'),
    path('publicaciones/', PublicacionListView.as_view(), name='publicacion_list'),
    path('publicaciones/<int:pk>/editar/', PublicacionUpdateView.as_view(), name='publicacion-editar'),
    path('publicaciones/<int:pk>/eliminar/', PublicacionDeleteView.as_view(), name='publicacion-eliminar'),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
