from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    Address     = models.CharField(max_length=130, verbose_name="Endereço")
    numberFone  = models.CharField(max_length=13, blank=True, null=True, verbose_name="Numero de celular")
    email       = models.EmailField(("Email"), blank=False)
    abstract    = models.TextField(blank=True, null=True, verbose_name="Resumo")

class Proficional(models.Model):
    occupation  = models.CharField(max_length=150, verbose_name="Cargo")
    company     = models.CharField(max_length=75, verbose_name="Empresa")
    functions   = models.TextField(blank=True, null=True, verbose_name="Funções")
    initialDate = models.DateField(verbose_name="Data Inicial")
    finaleDate  = models.DateField(blank=True, null=True, verbose_name="Data Final")
    user        = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.occupation

class Academica(models.Model):
    course      = models.CharField(max_length=150, verbose_name="Curso")
    university  = models.CharField(max_length=75, verbose_name="Universidade")
    initialDate = models.DateField(verbose_name="Data Inicial")
    finaleDate  = models.DateField(blank=True, null=True, verbose_name="Data Final")
    user        = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.course

class Qualificacoes(models.Model):
    title       = models.CharField(max_length=150, verbose_name="Titulo")
    company     = models.CharField(max_length=75, blank=True, null=True, verbose_name="Empresa")
    initialDate = models.DateField(verbose_name="Data Inicial")
    finaleDate  = models.DateField(blank=True, null=True, verbose_name="Data Final")
    user        = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.title