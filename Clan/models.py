from django.db import models
from Character.models import Character


class Clan(models.Model):
    clean_leader = models.ForeignKey(Character, on_delete=models.CASCADE)

    name = models.CharField(max_length=16)

    cafe_homepage = models.CharField(max_length=72, null=True, blank=True)

    emblem_url = models.CharField(max_length=128, null=True, blank=True, default='None')

    wins = models.IntegerField(default=0)

    losses = models.IntegerField(default=0)

    draws = models.IntegerField(default=0)

    points = models.IntegerField(default=0)

    total_points = models.IntegerField(default=0)

    level = models.IntegerField(default=0)

    exp = models.IntegerField(default=0)