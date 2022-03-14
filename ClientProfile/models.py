from django.db import models

# Create your models here for backend project
class ClientProfileModel(models.Model):
    name          = models.CharField(max_length=120, default=None)
    description   = models.TextField(blank=True, null=True)
    price         = models.DecimalField(decimal_places=2, max_digits=10 )
    history       = models.TextField(blank=True, null=True)
    summary       = models.TextField(blank=True, null=False)

    
 