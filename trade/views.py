import datetime

from django.shortcuts import render
from django.views import generic

from .models import Market, Order, Participant

from pyobsim import book as pyob_book
from pyobsim import order as pyob_order
from pyobsim import participant as pyob_participant

class IndexView(generic.ListView):
    """
    """
    template_name = "index.html"
    context_object_name = ""

    def get_queryset(self):
        """
        """
        return Market.objects.all()

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
        context["orders"] = Order.objects.filter(market=market_id, active=True).order_by("-type")

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

class OrderCreateView(generic.CreateView):
    """
    """
    model = Order
    fields = ["owner", "market", "type", "price", "quantity"]
    template_name = "orders/order_form.html"

    def form_valid(self, form):
        response = super(OrderCreateView, self).form_valid(form)
       
        # load book from database
        book_from_db = Market.objects.get(name=self.object.market)
        
        all_participants = [pyob_participant.Participant(p.id, p.name, p.balance, p.volume) for p in Participant.objects.filter(market=book_from_db.id)]
        all_orders = [pyob_order.Order(o.id, [p for p in all_participants if p.id == o.owner.id][0], book_from_db.name, o.type, o.price, o.quantity) for o in Order.objects.filter(market=book_from_db.id)]

        book = pyob_book.Book(book_from_db.name, all_participants)

        for o in all_orders:
            book.add(o)
        
        print(repr(book)) # DEBUG
        
        # write participants back to db
        for p in book.participants:
            corresponding_participant = Participant.objects.get(id=p.id)
            corresponding_participant.balance = p.balance
            corresponding_participant.volume = p.volume
            corresponding_participant.save()

        # write orders back to db
        for o in book.orders:
            print(repr(o)) # DEBUG
            corresponding_order = Order.objects.get(id=o.id)
            corresponding_order.quantity = o.qty
            print(corresponding_order.quantity) # DEBUG
            corresponding_order.save()

            # mark order as filled if it's filled
            if o.qty == 0:
                corresponding_order.active = False
                corresponding_order.filled = datetime.datetime.now()
                corresponding_order.save()

        # update current market price
        book_from_db.price = book.LTP
        book_from_db.save()

        return response

