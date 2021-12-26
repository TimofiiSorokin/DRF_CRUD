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
    serializer_class = EmployeeSerializer


class SettlementLogicApi(generics.ListAPIView):
    queryset = SettlementLogic.objects.all()
    serializer_class = EmployeeSerializer


class SettlementLogicUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = SettlementLogic.objects.all()
    serializer_class = EmployeeSerializer


class SettlementLogicDeleteApi(generics.DestroyAPIView):
    queryset = SettlementLogic.objects.all()
    serializer_class = EmployeeSerializer
