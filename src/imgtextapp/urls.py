from django.urls import path
from .views import img_text

urlpatterns = [
    path('makeText/', img_text, name='img_text'),
]