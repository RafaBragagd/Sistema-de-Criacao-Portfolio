from operator import index
from django.urls import path
from .views import IndexView

#Padrões de URL
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]