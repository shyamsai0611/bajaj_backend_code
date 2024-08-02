from django.urls import path
from . import views

urlpatterns = [
    path('bfhl/', views.details_view),
]
