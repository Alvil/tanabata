from django.urls import path

from .views import WishListView

app_name = 'wish'

urlpatterns = [
    path('', WishListView.as_view(), name='landing_page')
]
