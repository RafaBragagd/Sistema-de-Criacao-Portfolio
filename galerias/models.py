from django.db import models

# Create your models here.
class Classes(models.Model):
    name        = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Projetos(models.Model):
    title       = models.CharField(max_length=150)
    abstract    = models.TextField(blank=True, null=True, verbose_name="Descrição")
    kind        = models.ForeignKey('Classes', on_delete=models.PROTECT)
    user        = models.ForeignKey('usuarios.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Imagens(models.Model):
    image       = models.ImageField(upload_to='imagens/%d/%m/%Y/', verbose_name='Imagem', blank=True, null=True)
    projeto     = models.ForeignKey('Projetos', on_delete=models.CASCADE)

class Arquivos(models.Model):
    file       = models.FileField(upload_to='arquivo/%d/%m/%Y/', verbose_name='Arquivos', blank=True, null=True)
    projeto     = models.ForeignKey('Projetos', on_delete=models.CASCADE)