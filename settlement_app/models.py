from django.db import models
from payment_app.models import Payment

# Create your models here.
class Settlement(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    payment_settled = models.BooleanField(default=True)

    def __str__(self):
        return f"Settlement :{self.payment}"