from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

class CategoriaAPIView(APIView):

    #permission_classes = (IsAuthenticaded,)

    def get(self, request, pk=''):
        if pk == '': 
            categoria = Categoria.objects.all()
            serializer = CategoriaSerializer(categoria, many=True)
            return Response(serializer.data)
        else:
            categoria = Usuarios.objects.get(id=pk)
            serializer = CategoriaSerializer(categoria)
            return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data, many=True)
        serializer.is_valid()
        serializer.save()
        return Response({"msg":"Cadastrado com sucesso!"})

    def put(self, request, pk=''):
        categoria = Categoria.objects.get(id=pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        categoria = Categoria.objects.get(id=pk)
        categoria.delete()
        return Response({"msg":"Apagado com sucesso!"})


class AssinaturaAPIView(APIView):

    #permission_classes = (IsAuthenticaded,)

    def get(self, request, pk2=''):
        if pk2 == '': 
            assinatura = Assinatura.objects.all()
            serializer = AssinaturaSerializer(assinatura, many=True)
            return Response(serializer.data)
        else:
            assinatura = Assinatura.objects.get(id=pk2)
            serializer = AssinaturaSerializer(assinatura)
            return Response(serializer.data)

    def post(self, request):
        serializer = AssinaturaSerializer(data=request.data, many=True)
        serializer.is_valid()
        serializer.save()
        return Response({"msg":"Cadastrado com sucesso!"})

    def put(self, request, pk2=''):
        assinatura = Assinatura.objects.get(id=pk2)
        serializer = AssinaturaSerializer(assinatura, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk2=''):
        assinatura = Assinatura.objects.get(id=pk2)
        assinatura.delete()
        return Response({"msg":"Apagado com sucesso!"})

class FilmesAPIView(APIView):

    #permission_classes = (IsAuthenticaded,)

    def get(self, request, pk3=''):
        if pk3 == '': 
            filmes = Filmes.objects.all()
            serializer = FilmesSerializer(filmes, many=True)
            return Response(serializer.data)
        else:
            filmes = Filmes.objects.get(id=pk3)
            serializer = FilmesSerializer(filmes)
            return Response(serializer.data)

    def post(self, request):
        serializer = FilmesSerializer(data=request.data, many=True)
        serializer.is_valid()
        serializer.save()
        return Response({"msg":"Cadastrado com sucesso!"})

    def put(self, request, pk3=''):
        filmes = Filmes.objects.get(id=pk3)
        serializer = FilmesSerializer(filmes, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk3=''):
        filmes = Filmes.objects.get(id=pk3)
        filmes.delete()
        return Response({"msg":"Apagado com sucesso!"})


class UsuariosAPIView(APIView):

    #permission_classes = (IsAuthenticaded,)

    def get(self, request, pk=''):
        if pk == '': 
            usuarios = Usuarios.objects.all()
            serializer = UsuariosSerializer(usuarios, many=True)
            return Response(serializer.data)
        else:
            usuarios = Usuarios.objects.get(id=pk)
            serializer = UsuariosSerializer(usuarios)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosSerializer(data=request.data, many=True)
        serializer.is_valid()
        serializer.save()
        return Response({"msg":"Cadastrado com sucesso!"})

    def put(self, request, pk=''):       
        usuarios = Usuarios.objects.get(id=pk)
        serializer = UsuariosSerializer(usuarios, data=request.data)        
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)            

    def delete(self, request, pk=''):
        usuarios = Usuarios.objects.get(id=pk)
        usuarios.delete()
        return Response({"msg":"Apagado com sucesso!"})

class FavoritosAPIView(APIView):

    #permission_classes = (IsAuthenticaded,)

    def get(self, request, pk5=''):
        if pk5 == '': 
            favoritos = Favoritos.objects.all()
            serializer = FavoritosSerializer(favoritos, many=True)
            return Response(serializer.data)
        else:
            favoritos = Favoritos.objects.get(id=pk5)
            serializer = FavoritosSerializer(favoritos)
            return Response(serializer.data)

    def post(self, request):
        serializer = FavoritosSerializer(data=request.data, many=True)
        serializer.is_valid()
        serializer.save()
        return Response({"msg":"Cadastrado com sucesso!"})

    def put(self, request, pk5=''):
        favoritos = Favoritos.objects.get(id=pk5)
        serializer = FavoritosSerializer(favoritos, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk5=''):
        favoritos = Favoritos.objects.get(id=pk5)
        favoritos.delete()
        return Response({"msg":"Apagado com sucesso!"})