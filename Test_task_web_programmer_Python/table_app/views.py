from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import TableSerializer

"add connection Table (mysql)"
from .models import Table

# Create your views here.


# django rest
class TableView(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

# vue js
def table_vue(request):
    return render(request, 'table_app/table.html')  # html template output



