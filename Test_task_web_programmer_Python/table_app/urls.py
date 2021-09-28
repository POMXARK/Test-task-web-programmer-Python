from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # function call
    # connection  add page transition tracking
]