from django.urls import path
from .views import*

urlpatterns = [
    path('categoria/', CategoriaAPIView.as_view(), name='categoriaa'),
    path('categoria/<int:pk>', CategoriaAPIView.as_view(), name='categoria Parameters'), 

    path('assinatura/', AssinaturaAPIView.as_view(), name='assinaturaa'),
    path('assinatura/<int:pk2>', AssinaturaAPIView.as_view(), name='assinaturaParameters'), 

    path('filmes/', FilmesAPIView.as_view(), name='filmess'),
    path('filmes/<int:pk3>', FilmesAPIView.as_view(), name='filmesParameters'), 

    path('usuarios/', UsuariosAPIView.as_view(), name='usuarioss'),
    path('usuarios/<int:pk>', UsuariosAPIView.as_view(), name='usuariosParameters'), 

    path('favoritos/', FavoritosAPIView.as_view(), name='favoritoss'),
    path('favoritos/<int:pk5>', FavoritosAPIView.as_view(), name='favoritosParameters'), 

]