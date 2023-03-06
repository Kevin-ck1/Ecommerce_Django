from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<int:listing_id>",views.listing_page, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("bidlist", views.bidlist, name="bidlist"),
    path("closeListing", views.close_lisiting, name="close"),
    path("myListing", views.my_listing, name="myListing"),
    path("comments", views.comments, name="comments"),
    path("cateogries", views.category, name="category")
]
