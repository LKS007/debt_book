from django.db import models
from django.contrib.auth.models import User

class Debt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    debtor = models.CharField('who owned money',max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()