from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sender_id = models.CharField(max_length=100)
    recipient_id = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100,default="PENDING")

    def __str__(self):
        return f"Payment amount:{self.amount}, sender_id:{self.sender_id}, recepient_id:{self.recipient_id}, id:{self.id}, created_on:{self.created_on}"

