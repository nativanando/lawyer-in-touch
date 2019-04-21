from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):

    class Meta:
        db_table =   'customer'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone = models.TextField(blank=True, null=True)
    is_facebook_auth = models.BooleanField(default=False, null=True)
    is_google_auth = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user)

class Lawyer(models.Model):

    class Meta:
        db_table = 'lawyer'

    user = models.OneToOneField(User, related_name='lawyer', on_delete=models.CASCADE)
    cna = models.TextField(blank=False, null=False)
    phone = models.TextField(blank=True, null=True)
    is_facebook_auth = models.BooleanField(default=False, null=True)
    is_google_auth = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user)

class Contract(models.Model):

    class Meta:
        db_table = 'contract'

    lawyer = models.ForeignKey(Lawyer,on_delete=models.CASCADE, related_name='contracts')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='contracts')
    contract_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.id)
