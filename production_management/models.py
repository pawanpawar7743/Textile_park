
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class WorkOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    scheduled_start_date = models.DateField()
    scheduled_end_date = models.DateField()


class ProductionRecord(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    actual_start_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

