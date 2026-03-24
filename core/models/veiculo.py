from django.db import models


class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, null=True, blank=True)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE, null=True, blank=True)
    acessorio = models.ManyToManyField('Acessorio', blank=True)

    def __str__(self):
        return str(self.id) + " " + self.modelo.nome + " " + self.cor.nome
