import json

from rest_framework import serializers
from .models import SettlementLogic


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettlementLogic
        fields = ('id', 'first_item', 'second_item')

    def create(self, validated_data):
        nums_start = json.loads(validated_data.get('first_item'))
        target_start = int(validated_data.get('second_item'))
        nums, target = nums_start, target_start
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append([i, j])
        result = {
            'first_item': str(nums_start),
            'second_item': str(target_start),
            'result_item': str(answer[0])
        }
        settlement = SettlementLogic.objects.create(**result)
        return settlement


