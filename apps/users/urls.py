from django.urls import path

from apps.users.views import (UsersAddCarView, UserCreateView,
                              UserListView)

urlpatterns = [
    path('', UserCreateView.as_view(), name='user_create'),
    path('/list', UserListView.as_view(),  name='users_list'),
    path('/<int:pk>/cars', UsersAddCarView.as_view(), name='users_add_car'),
]