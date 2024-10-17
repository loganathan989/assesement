from django.db import models

import uuid


class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=255, default=uuid.uuid4)
    website = models.URLField(blank=True, null=True)


    class Meta:
        db_table = "Account"