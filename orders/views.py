from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from models import Order, Writer, Client


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, "order_list.html", {"orders": orders})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "order_detail.html", {"order": order})


@login_required
def writer_dashboard(request):
    writer = get_object_or_404(Writer, user=request.user)
    orders = Order.objects.filter(writer=writer)
    return render(request, "writer_dashboard.html", {"orders": orders})


@login_required
def client_dashboard(request):
    client = get_object_or_404(Client, user=request.user)
    orders = Order.objects.filter(client=client)
    return render(request, "client_dashboard.html", {"orders": orders})
