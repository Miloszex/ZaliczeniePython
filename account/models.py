from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class ExtendedUser(models.Model):

    YEAR_CHOICE = (
        (0, 'undefined'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    index_number = models.CharField(max_length=6, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICE, default=0)

    def __str__(self):
        return self.user.username + ' - ' + self.index_number 
