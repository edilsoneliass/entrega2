from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='listar_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detalhes_post'),
    path('post/novo/', PostCreateView.as_view(), name='criar_post'),
    path('post/editar/<int:pk>/', PostUpdateView.as_view(), name='editar_post'),
    path('post/deletar/<int:pk>/', PostDeleteView.as_view(), name='deletar_post'),
]