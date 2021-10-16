from django.db import models
from Account.models import Account


class Character(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    character_id = models.IntegerField()

    name = models.CharField(max_length=16)

    level = models.IntegerField()

    bounty = models.IntegerField(default=0)

    kills = models.IntegerField()

    deaths = models.IntegerField()

    reg_date = models.DateTimeField()

    delete_flag = models.IntegerField(default=0)