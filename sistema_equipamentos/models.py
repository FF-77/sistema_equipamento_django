from django.db import models

# Create your models here.

class Cadastro(models.Model):

    setor = [
        ('TI', 'Tecnológia Informação '),
        ('RH', 'Recursos Humanos'),
        ('GE', 'Gerência'),
        ('ES', 'Escritório'),
        ('PR', 'Produção'),        
    ]

    data = models.DateTimeField(auto_now_add=False)
    responsavel = models.CharField(max_length=120)
    equipamento = models.CharField(max_length=100)
    setor = models.CharField(max_length=2, choices=setor, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)

    class Meta:

        verbose_name = 'Cadastro'

    def __str__(self):

        return self.responsavel