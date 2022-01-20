from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    # we need to actually override that default string method with our own
    """
    this is going to return the item class's name attribute which in our case
    is going to be the name that we put into the form
    """
    def __str__(self):
        return self.name
