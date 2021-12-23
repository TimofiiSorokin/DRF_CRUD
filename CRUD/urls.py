from django.urls import path

from CRUD.views import TwoSumView, SettlementLogicCreateApi, SettlementLogicApi, SettlementLogicUpdateApi, \
    SettlementLogicDeleteApi

urlpatterns = [
    # for test TwoSumView
    path('two-sum-test', TwoSumView.as_view(), name='two-sum-test'),
    # working points
    path('two-sum', SettlementLogicApi.as_view(), name='two-sum'),
    path('two-sum/create', SettlementLogicCreateApi.as_view(), name='two-sum-create'),
    path('two-sum/<int:pk>', SettlementLogicUpdateApi.as_view(), name='current-two-sum'),
    path('two-sum/<int:pk>/delete', SettlementLogicDeleteApi.as_view(), name='two-sum-delete'),
]
