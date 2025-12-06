from django.urls import path
from . import views

urlpatterns = [
    # Autenticación
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('guardar-usuario/', views.guardar_usuario, name='guardar_usuario'),  # IMPORTANTE
    path('logout/', views.logout_view, name='logout'),
    
    # Páginas principales
    path('home/', views.seleccionar_generos, name='home'),  # Esta es la de géneros
    path('guardar-generos/', views.guardar_generos, name='guardar_generos'),
    path('lista-reproduccion/', views.lista_reproduccion, name='lista_reproduccion'),
    
    path('buscar-canciones/', views.buscar_canciones, name='buscar_canciones'),
    path('reaccionar-cancion/', views.reaccionar_cancion, name='reaccionar_cancion'),
    path('calificar-cancion/', views.calificar_cancion, name='calificar_cancion'),
    path('rating-estadisticas/<int:cancion_id>/', views.obtener_estadisticas_rating, name='estadisticas_rating'),

    path('audio/<path:ruta>/', views.servir_audio, name='servir_audio'),

    
]
