from django.db import models
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta

class PhoneNumber(models.Model):
    user = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15, unique=True)
    purchase_date = models.DateTimeField(default=now)
    next_billing_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.next_billing_date:
            self.next_billing_date = self.purchase_date + relativedelta(minutes=1)
        super().save(*args, **kwargs)
