from django.db import models


class SettlementLogic(models.Model):
    first_item = models.TextField()
    second_item = models.TextField()
    result_item = models.TextField()

    class Meta:
        db_table = 'SettlementLogic'
