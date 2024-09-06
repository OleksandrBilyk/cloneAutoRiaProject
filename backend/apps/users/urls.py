from django.urls import path

from apps.users.views import (UserAddAvatarView, UserBlockView,
                              UserListCreateView, UsersAddCarView,
                              UserUnBlockView)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/avatars', UserAddAvatarView.as_view(), name='user_add_avatar'),
    path('/<int:pk>/cars', UsersAddCarView.as_view(), name='users_add_car'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='user_block'),
    path('/<int:pk>/unblock', UserUnBlockView.as_view(), name='user_unblock'),
]