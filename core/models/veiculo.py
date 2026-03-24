from django.db import models


class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    categoria = models.CharField(max_length=80)

    def __str__(self):
        return str(self.id) + " " + self.nome
