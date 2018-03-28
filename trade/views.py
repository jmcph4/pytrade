from django.shortcuts import render
from django.views import generic

from .models import Market, Order

class MarketIndexView(generic.ListView):
    """
    Index view for the markets
    """
    template_name = "markets/index.html"
    context_object_name = "global_markets_list"

    def get_queryset(self):
        """
        Return all markets
        """
        return Market.objects.all()

class MarketDetailView(generic.DetailView):
    """
    Detail view for markets (this is where the order book will be displayed)
    """
    model = Market
    template_name = "markets/detail.html"

    def get_context_data(self, **kwargs):
        # get default context data
        context = super(MarketDetailView, self).get_context_data(**kwargs)
        
        # add order list to context data
        market_id = context["market"].id
        context["orders"] = Order.objects.filter(market=market_id).order_by("-type")

        return context

class OrderIndexView(generic.ListView):
    """
    """
    template_name = "orders/index.html"
    context_object_name = "global_orders_list"

    def get_queryset(self):
        """
        Return all active orders, newest to oldest
        """
        return Order.objects.all().filter(active=True).order_by("-created")

class OrderDetailView(generic.DetailView):
    """
    Detail view for orders, displays information on particular order
    """
    model = Order
    template_name = "orders/detail.html"

