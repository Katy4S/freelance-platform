from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom user model
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


# Writer model
class Writer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user


# Client model
class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


# Order model
class Order(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Message model for communication between client and writer
class Message(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} in order {self.order.title}"
