from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

class Subject(models.Model):

    DAY_CHOICE = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
    )
    name = models.CharField(max_length=150)
    day = models.IntegerField(choices=DAY_CHOICE)
    begin_at = models.TimeField(blank=True)
    end_at = models.TimeField(blank=True)
    actual_space = models.IntegerField(default=0)
    space = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' - ' + str(self.day) + ' ' + str(self.begin_at) + '-' + str(self.end_at)


class Sign(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subject', 'user')

    def __str__(self):
        return self.user.first_name + ' '+ self.user.last_name + ' - ' + self.subject.name + ' ' + str(self.subject.begin_at) +':'+ str(self.subject.end_at)

