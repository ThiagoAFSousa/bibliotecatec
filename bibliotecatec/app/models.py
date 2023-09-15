from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50,blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50,blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Leitor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    preco = models.PositiveIntegerField()
    data_pub = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.autor} - {self.nome}'

class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.leitor} / {self.livro} / {self.data_emprestimo} / {self.data_devolucao} '


    
    