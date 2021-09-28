from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

# check ( http://127.0.0.1:8000/?format=json )
router = SimpleRouter()  # django rest
router.register('api/table', views.TableView)

urlpatterns = [
    #path('',views.index),#, views.index),  # function call
    path('', views.table_vue),  # function call
    # connection  add page transition tracking
]

urlpatterns += router.urls
