from django.urls import path

from .views import WishCreateView
from .views import WishListView


app_name = 'wish'

urlpatterns = [
    path('', WishListView.as_view(), name='landing-page'),
    path('wish/', WishCreateView.as_view(), name='create-wish'),
]
