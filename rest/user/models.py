from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    ''' Create and returns a user with an email, username and password ''' 

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    USERNAME_FIELD = 'email'
    
    '''Tells Django that the UserManager class defined above should manage objects of this type '''
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:

        db_table = "login"