from django.urls import path

from apps.user_auto_lots.views import (AutoLotsListCreateView,
                                       AutoParkAddCarView)

urlpatterns = [
    path('', AutoLotsListCreateView.as_view(), name='auto_lots_list_create'),
    path('/<int:pk>/add_car', AutoParkAddCarView.as_view(), name='auto_park_add_car'),
]
