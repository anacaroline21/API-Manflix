from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

class Assinatura(models.Model):
    nome = models.CharField(max_length=15)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
class Filmes(models.Model):
    nome = models.CharField(max_length=55)
    categoriaFK = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

class Usuarios(models.Model):
    nome = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    fone = models.CharField(max_length=55)
    ativo = models.BooleanField(default=False)
    assinaturaFK = models.ForeignKey(Assinatura, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nome


class Favoritos(models.Model):
    nome = models.CharField(max_length= 100)
    filmeFK = models.ForeignKey(Filmes, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)