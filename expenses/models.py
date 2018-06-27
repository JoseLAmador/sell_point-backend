from django.db import models
from django.core.validators import RegexValidator

class Provider(models.Model):
    provider = models.CharField(max_length=140, blank=True)
    address = models.CharField(max_length=140, blank=True)
    rfc = models.CharField(max_length=20, blank=True, unique=True)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)

    def __str__(self):
        return self.provider

    class Meta:
        ordering = ['-id']

class Expense (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    provider_expense = models.ForeignKey(Provider, related_name='expenses', on_delete=models.PROTECT, blank=True)
    expense_check = models.BooleanField(default=False)
    no_check = models.CharField(max_length=140, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "Expense no. {}".format(self.id)

    class Meta:
        ordering = ['-id']









