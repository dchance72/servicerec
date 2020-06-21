from django.db import models
from django.conf import settings
import datetime
# Create your models here.

"""
A user's status distinguishes between active users (e.g. currently
employed) vs. inactive (perhaps no longer with the organization)
employees.  We cannot simply purge users from the database, since their
IDs are referenced as a foreign key by another table.
class User(models.Model):
    USER_STATUS = (
        (0, "Active"),
        (1, "Inactive"),
    )
    name = models.CharField(max_length=64)
    status = models.IntegerField(choices=USER_STATUS, default=0)
    def __str__(self):
        return self.name
"""


class Firearm(models.Model):
    make = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    serial = models.CharField(max_length=32)
    location = models.CharField(max_length=64, default=None, null=True)
    def __str__(self):
        return self.make + ' ' + self.model
    class Meta:
        ordering = ['make']


class CheckEvent(models.Model):
    STATE_CODES = (
        ( 0, 'Ready' ),
        ( 1, 'Malfunctioning' ),
        ( 2, 'Not loaded' ),
        ( 3, 'Not In Service' ),
        ( 4, 'In for Repair' ),
        ( 5, 'Non-functional' ),
        ( 6, 'Decommissioned' ),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    when = models.DateTimeField(default=datetime.datetime.now)
    firearm = models.ForeignKey(Firearm, on_delete=models.CASCADE)
    notes = models.CharField(max_length=200,blank=True)
    state = models.IntegerField(choices=STATE_CODES, default=0)
    def __str__(self):
        return self.firearm.serial + '(' + str(self.when) + ')'
    class Meta:
        ordering = ['when']

