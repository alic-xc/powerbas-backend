from django.urls import path
from .views import AdvertDetailtView, AdvertListView, CreateAdvertView


app_name = 'fingerprints'

urlpatterns = [
    path('advert/add', CreateAdvertView.as_view(), name='add_advert'),
    path('advert/lists', AdvertListView.as_view(), name='adverts'),
    path('advert/<id>/', AdvertDetailtView.as_view(), name='advert'),
]