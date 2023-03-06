from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    pass

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    list_category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.list_category}"

class AuctionListing(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    start_price = models.IntegerField()
    current_bid = models.IntegerField()
    photo = models.CharField(max_length=255, null = True, blank=True)
    display_button = models.BooleanField(default=True) 
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_creator")
    listing_category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, blank=True, related_name="item_category")
    listing_open = models.BooleanField(default=True) 
    
    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    id = models.BigAutoField(primary_key=True)
    bid_item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name="listing_bidder")
    watchBidder = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=0, related_name="listing_watchBidder")
    bid_price = models.IntegerField(null=True, blank=True)
    bid_identifier = models.IntegerField()
    
    def __str__(self):
        return f"{self.bid_item}"

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=64)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_commentor")
    comment_item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="listing_comment")

    def __str__(self):
        return f"{self.comment}"

class Info(models.Model):
    id = models.BigAutoField(primary_key=True)
    won_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    author_Username = models.CharField(max_length=64)
    author_Email = models.CharField(max_length=64)
    winner_Username = models.CharField(max_length=64)
    winner_Email = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.won_listing} {self.author_Username} {self.winner_Username}"



