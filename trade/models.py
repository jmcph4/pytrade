from django.db import models

class Trader(models.Model):
    """
    Represents a trader in the marketplace.

    Essentially wraps PyOBSim's Participant class.
    """
    name = CharField(unique=True)
    balance = DecimalField()
    volume = IntegerField()

class Market(models.Models):
    """
    Represents a market to be traded in.

    Essentially wraps PyOBSim's Book class.
    """
    name = CharField()
    traders = ManyToManyField(Market)


