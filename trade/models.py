from datetime import datetime

from django.db import models

class Trader(models.Model):
    """
    Represents a trader in the marketplace.

    Essentially wraps PyOBSim's Participant class.
    """
    name = models.CharField(max_length=32, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    def __str__(self):
        return self.name

class Market(models.Model):
    """
    Represents a market to be traded in.

    Essentially wraps PyOBSim's Book class.
    """
    name = models.CharField(max_length=5)
    traders = models.ManyToManyField(Trader)

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Represents an order for a given market.

    Essentially wraps PyOBSim's Order class.
    """
    owner = models.ForeignKey(Trader, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    type = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    # metadata
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    filled = models.DateTimeField(blank=True, null=True)
    cancelled = models.DateTimeField(blank=True, null=True)

    """
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()

        return super(Order, self).save(*args, **kwargs)
    """

    def __str__(self):
        s = "Order({0}, {1}, {2}, {3}, {4})".format(str(self.owner),
                str(self.market), self.type, self.price, self.quantity)
        return s

