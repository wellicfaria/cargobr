from django.db import models
import string
import random


# Create your models here.
class Carga(models.Model):
	
	id_carga = models.CharField(max_length=6,unique=True)
	valor = models.DecimalField(max_digits=15,decimal_places=2)
	dados = models.TextField()
	usuario = models.ForeignKey('auth.User')
	def cadastro(self):
		self.id_carga = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
		self.save()

	def __str__(self):
		return self.id_carga