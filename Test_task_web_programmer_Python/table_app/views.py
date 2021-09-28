from django.shortcuts import render

"add connection Table (mysql)"
from .models import Table


# Create your views here.


def index(request):
    table_rows = Table.objects.all()  # get all objects from the database
    return render(request, 'table_app/table.html',
                  {'table': 'Таблица', 'table_rows': table_rows})  # html template output


def table_vue(request):
    table_rows = Table.objects.all()  # get all objects from the database
    return render(request, 'table_app/table.html')  # html template output
