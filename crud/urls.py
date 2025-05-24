from django.urls import path
from .views.auth_views import*
from .views.main_views import*
from .views.auth_views import*


from .views.auth_views import*

from django.urls import path
from . import views  # import your views from the current app

urlpatterns = [
    path('register/', register),
    path('create/', create_blog),
]
