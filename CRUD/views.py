import json

from rest_framework.response import Response
from .serializer import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import SettlementLogic


class TwoSumView(APIView):
    # TEST
    def get(self, request):
        response_json = {
            "teqst": {
                "test": [
                    0,
                    100000
                ]
            },
            "test": {
                "teswt": {
                    "test": [
                        0,
                        10000
                    ]
                },
                "test": {
                    "range": [
                        0,
                        1000
                    ]
                }},
            "QQQQ": [
                    {
                        "currency": "ADR",
                        "label": "ADR",
                        "value": 10
                    },
                    {
                        "currency": "WWW",
                        "label": "WWW",
                        "value": 21
                    }
                ]
        }
        return Response(response_json, status=status.HTTP_200_OK)


class SettlementLogicCreateApi(generics.CreateAPIView):
    queryset = SettlementLogic.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        nums_start = json.loads(request.data.get('first_item'))
        target_start = int(request.data.get('second_item'))
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
        sl = SettlementLogic.objects.create(**result)
        sl.save()
        return Response(result, status=status.HTTP_200_OK)


class SettlementLogicApi(generics.ListAPIView):
    queryset = SettlementLogic.objects.all()
    serializer_class = EmployeeSerializer


class SettlementLogicUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = SettlementLogic.objects.all()
    serializer_class = EmployeeSerializer


class SettlementLogicDeleteApi(generics.DestroyAPIView):
    queryset = SettlementLogic.objects.all()
    serializer_class = EmployeeSerializer
