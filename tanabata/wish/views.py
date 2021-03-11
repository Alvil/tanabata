from django.shortcuts import render
from django.views import generic

from .models import Wish


class WishListView(generic.ListView):
    model = Wish
    template_name = 'wish/landing_page.html'
