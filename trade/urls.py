from django.urls import path

from . import views

app_name = "trade"
urlpatterns = [path("", views.IndexView.as_view(),
                    name="index"),
                path("markets/", views.MarketIndexView.as_view(),
                    name="markets_index"),
                path("markets/<int:pk>", views.MarketDetailView.as_view(),
                    name="markets_detail"),
                path("orders/", views.OrderIndexView.as_view(),
                    name="orders_index"),
                path("orders/<int:pk>", views.OrderDetailView.as_view(),
                    name="orders_detail"),
                path("orders/create/", views.OrderCreateView.as_view(),
                    name="orders_create")]

