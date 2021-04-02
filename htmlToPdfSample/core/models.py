from django.db import models
from django.contrib.auth.models import User


class Foo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

    def __str__(self):
        return f'{self.user.username} | XOF {self.amount} '
