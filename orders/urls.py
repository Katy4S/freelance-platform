from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("order/<int:pk>/", views.order_detail, name="order_detail"),
    path("writer-dashboard/", views.writer_dashboard, name="writer_dashboard"),
    path("client-dashboard/", views.client_dashboard, name="client_dashboard"),
    path("clients/", views.client_list, name="client_list"),
]

