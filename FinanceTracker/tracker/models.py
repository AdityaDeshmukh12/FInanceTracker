from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.description} - {self.amount}"
