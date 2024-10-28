from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Client, Writer, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    num_clients = Client.objects.count()
    num_writers = Writer.objects.count()
    num_orders = Order.objects.count()
    return render(request, "orders/index.html", {
        "num_clients": num_clients,
        "num_writers": num_writers,
        "num_orders": num_orders
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


def client_list(request):
    clients = Client.objects.all()
    return render(request, "orders/client_list.html", {"clients": clients})


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
