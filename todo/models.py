from django.db import models

# Create your models here.
# Will create a table call Item in the SQL Database 
# Import django model class so we can use it's functionality
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False) #prevent blank creations 
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name