from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    initial_bid = models.FloatField()
    category = models.CharField(max_length=64)
    image_url = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    price = models.FloatField()
    auction_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='auction_listing')
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.auction_listing}: {self.price}"

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.comment}"
