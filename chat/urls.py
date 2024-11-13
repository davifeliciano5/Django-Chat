from .views import IndexView, SalaView
from django.urls import path

urlpatterns = [
    path('',IndexView.as_view(),name = 'index')
    path('chat/<str:nome_sala>/',SalaView.as_view(),name = 'sala')
]