from django.db import models


class Instrumento(models.Model):
    CATEGORIA_CHOICES = [
        ('corda', 'Corda'),
        ('sopro', 'Sopro'),
        ('percussao', 'Percussão'),
        ('teclas', 'Teclas'),
        ('outros', 'Outros'),
    ]

    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    imagem = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'
