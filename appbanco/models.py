from django.db import models
from uuid import uuid4
from django.core.validators import RegexValidator


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid4(), primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Client(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    cpf = models.CharField('CPF', help_text='Formato: 00011122233', unique=True, validators=[RegexValidator(regex="^.{11}$")], max_length=13)
    balance = models.DecimalField(decimal_places=2, max_digits=9)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Transaction(BaseModel):
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="transaction_sender")
    receiver = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="transaction_receiver")
    value = models.DecimalField(decimal_places=2, max_digits=9)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"


class Deposit(BaseModel):
    receiver = models.ForeignKey(Client, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=2, max_digits=9)

    class Meta:
        verbose_name = "Deposit"
        verbose_name_plural = "Deposits"
