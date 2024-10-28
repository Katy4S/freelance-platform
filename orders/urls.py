from django.urls import path
import views

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("order/<int:pk>/", views.order_detail, name="order_detail"),
    path("writer-dashboard/", views.writer_dashboard, name="writer_dashboard"),
    path("client-dashboard/", views.client_dashboard, name="client_dashboard"),
]
