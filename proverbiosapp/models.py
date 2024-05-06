from django.db import models

class Justica(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
    
class Preguica(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
   

class Sabedoria(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
     

class Sabio(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo

class Vizinho(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
    
class Disciplina(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
    
class Família(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
    
    
class Amigos(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
    
    

class Emprestimo(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
    
    

class Trabalho(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
    
    
    
class Investimento(models.Model):
    versiculo = models.CharField(max_length=60, null=True)
    contexto = models.TextField(null=True)
    aplicacao= models.TextField(null=True)

    def __str__(self):
        return self.versiculo
    


