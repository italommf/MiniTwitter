from django.urls import path
from .views import UsuarioCriarView

urlpatterns = [
    path('registro/', UsuarioCriarView.as_view(), name = 'registro'),
]