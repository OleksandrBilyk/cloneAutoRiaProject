
from django.urls import include, path

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    # path('users', include('apps.users.urls'))
    path('auto_lots', include('apps.user_auto_lots.urls'))
]