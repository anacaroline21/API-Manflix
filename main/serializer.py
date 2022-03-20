from rest_framework import serializers
from .models import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Categoria
        fields = '__all__'

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Assinatura
        fields = '__all__'

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Filmes
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'

class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Favoritos
        fields = '__all__'

