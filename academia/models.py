from django.db import models

class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)

    class instituicao(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField()
        data_nascimento = models.DateField(blank= True, null= True)

    def __str__(self):
        return self.nome

    class Meta:
            verbose_name_plural = 'Instituições'