from django.db import models
from django.contrib.auth.models import User


EXPENSE_TYPE_CHOICES = (
    ('Hospedaje', 'Hospedaje'),
    ('Alimentación', 'Alimentación'),
    ('Transporte', 'Transporte'),
)


class AuthorizedTravel(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date_requested = models.DateField()
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    transportation_mode = models.CharField(max_length=255)
    purpose = models.TextField(blank=True)


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class TravelExpense(models.Model):
    travel = models.ForeignKey(AuthorizedTravel, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=255, choices=EXPENSE_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    receipt = models.FileField(upload_to='receipts/', blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(expense_type__in=[choice[0] for choice in EXPENSE_TYPE_CHOICES]), name='valid_expense_type')
        ]

    def total_amount(self):
        return self.amount + self.iva