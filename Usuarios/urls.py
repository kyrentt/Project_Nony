from django.urls import path
from .views import (
    HomeView,
    ArticleDetailView,
    AddPostView,
    etiqueta,
    UpdatePostView,
    DeletePostView,
    perfil,
    perfil2,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update-post"),
    path("article/delete/<int:pk>", DeletePostView.as_view(), name="delete-post"),
    path("etiquetas/", etiqueta, name="eti"),
    path('perfil/', perfil, name='perfil'),
    path('perfil_de_otro_usuario/<str:name>/', perfil2, name='per2'),
]
