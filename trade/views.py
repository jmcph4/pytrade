from django.shortcuts import render
from django.views import generic

from .models import Market

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

