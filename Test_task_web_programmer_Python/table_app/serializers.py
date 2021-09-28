from rest_framework.serializers import ModelSerializer
from .models import Table


# new Serializer
class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id','date', 'title', 'quantity', 'distance']
