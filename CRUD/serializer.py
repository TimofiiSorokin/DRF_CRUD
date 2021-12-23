from rest_framework import serializers
from .models import SettlementLogic


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettlementLogic
        fields = '__all__'


