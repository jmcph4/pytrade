from django.db import models

class Trader(models.Model):
    """
    Represents a trader in the marketplace.

    Essentially wraps PyOBSim's Participant class.
    """
    name = models.CharField(max_length=32, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

class Market(models.Model):
    """
    Represents a market to be traded in.

    Essentially wraps PyOBSim's Book class.
    """
    name = models.CharField(max_length=5)
    traders = models.ManyToManyField(Trader)

