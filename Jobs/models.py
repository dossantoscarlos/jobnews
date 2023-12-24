from django.db import models
from datetime import datetime

###### Model Empresa ######
class Empresa(models.Model):
    nome = models.CharField('nome', max_length=100)
    descricao = models.TextField('descricao')
    status = models.BooleanField('status', default=True)
    created_at = models.DateTimeField('created_at', default=datetime.now())
    
    class Meta:
        pass

class Contato(models.Model):
    tipo = models.CharField('tipo', max_length=100)
    valor= models.CharField('valor', max_length=255)
    created_at = models.DateTimeField('created_at', default=datetime.now())

    class Meta :
        pass

class Candidato(models.Model):
    nome = models.CharField('nome', max_length=100)
    created_at = models.DateTimeField('created_at', default=datetime.now())    

    class Meta:
        pass

###### Model Jobs ######
class Job(models.Model):
    descricao = models.TextField('descricao')
    beneficio = models.TextField('beneficio')
    titulo = models.CharField('titulo', max_length=100)
    created_at = models.DateTimeField('created_at',default = datetime.now())
    especializacao = models.TextField('especializacao')
    
    class Meta: 
        pass

class Categoria(models.Model):

    class Meta:
        pass
