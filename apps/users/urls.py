from django.urls import path

from apps.users.views import (UsersAddCarView, UsersListCreateView,
                              UsersRetrieveUpdateDestroyView)

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>', UsersRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_delete'),
    path('/<int:pk>/cars', UsersAddCarView.as_view(), name='users_add_car'),
]