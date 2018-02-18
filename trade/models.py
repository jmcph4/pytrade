from django.db import models

class Trader(models.Model):
    """
    Represents a trader in the marketplace.

    Essentially wraps PyOBSim's Participant class.
    """
    name = CharField(unique=True)
    balance = DecimalField()
    volume = IntegerField()

