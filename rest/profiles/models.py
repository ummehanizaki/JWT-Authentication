import uuid
from django.db import models
from user.models import User

class UserProfile(models.Model):

    class Meta:
        db_table = "profiles"