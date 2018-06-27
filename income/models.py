from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Cliente(models.Model):
    client = models.CharField(max_length=140, blank=True)
    address = models.CharField(max_length=140, blank=True)
    rfc = models.CharField(max_length=140, unique=True, blank=True)
    email = models.EmailField(max_length=50, blank=True, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)

    def __str__(self):
        return self.client

    class Meta:
        ordering = ["-id"]

class Income (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Cliente, related_name='incomes', blank=True, on_delete=models.PROTECT)
    income_check = models.BooleanField(default=False)
    no_icheck = models.CharField(max_length=140, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "Income no. {}".format(self.id)

    class Meta:
        ordering = ['-id']
