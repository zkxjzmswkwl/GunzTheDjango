from django.db import models


class Account(models.Model):
    # AID
    account_id = models.IntegerField()

    # UserID
    user_id = models.CharField(max_length=32)

    # UGradeID
    ugrade = models.IntegerField(default=0)

    # PGradeID
    pgrade = models.IntegerField(default=0)

    # RegDate
    reg_date = models.DateTimeField()

    # Country 
    country = models.CharField(max_length=32)

    # LastLoginTime
    last_login = models.DateTimeField()

    # LastLogoutTime
    last_logout = models.DateTimeField()

    # IsBanned
    is_banned = models.BooleanField(default=False)

    # BannedReason
    ban_reason = models.CharField(max_length=280)