import pytest

from CRUD.models import SettlementLogic
from django.urls import reverse


@pytest.mark.django_db
def test_create_settlement():
    body_items = {
        "id": 1,
        "first_item": "[2,7,11,15]",
        "second_item": "9",
        "result_item": "[0, 1]"
    }
    SettlementLogic.objects.create(**body_items)
    assert SettlementLogic.objects.count() == 1


@pytest.mark.django_db
def test_get_settlement_url(client):
    url = reverse('two-sum')
    response = client.get(url)
    assert response.status_code == 200

