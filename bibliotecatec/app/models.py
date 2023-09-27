from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome_cidade}, {self.uf}"

class Autor(models.Model):
    nome_autor = models.CharField(max_length=100)
    site_autor = models.CharField(max_length=100)
    cidade_autor = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_autor
    
class Genero(models.Model):
    nome_genero = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_genero
    
class Editora(models.Model):
    nome_editora = models.CharField(max_length=100)
    site_editora = models.CharField(max_length=100)
    cidade_editora = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_editora
    
class Leitor(models.Model):
    nome_leitor = models.CharField(max_length=100)
    email_leitor =  models.CharField(max_length=100)
    cpf_leitor = models.CharField(max_length=11, unique=True)
    def __str__(self):
        return self.nome_leitor

class Livro(models.Model):
    nome_livro = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    preco = models.IntegerField()
    data_plub = models.DateField()
    status = models.BooleanField()
    def __str__(self):
        return self.nome_livro

class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    leitor= models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.leitor}, {self.livro}"

    


