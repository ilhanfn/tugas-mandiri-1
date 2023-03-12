from django.db import models

class Expense(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
