from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Wish


class WishListView(generic.ListView):
    model = Wish
    template_name = 'wish/landing_page.html'


class WishCreateView(generic.CreateView):
    model = Wish
    fields = ['wish', ]
    template_name = 'wish/wish_create_view.html'
    success_url = reverse_lazy('wish:landing-page')

    def form_valid(self, form):
        wish_object = form.save(commit=False)
        try:
            wish_exist = Wish.objects.get(wish__iexact=wish_object.wish)
            wish_exist.times_wished += 1
            wish_exist.save()
            # need to manually declare what would be returned
            # otherwise it will create another object instance
            # on top of increasing the times_wished
            return HttpResponseRedirect(reverse_lazy('wish:landing-page'))
        except ObjectDoesNotExist:
            return super().form_valid(form)
