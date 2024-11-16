from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_posts, name='listar_posts'),
    path('post/<int:id>/', views.detalhes_post, name='detalhes_post'),
    path('post/<int:id>/comentario/novo/', views.criar_comentario, name='criar_comentario'),
    path('post/novo/', views.criar_post, name='criar_post'),
    path('post/editar/<int:id>/', views.editar_post, name='editar_post'),
    path('post/deletar/<int:id>/', views.deletar_post, name='deletar_post'),
]