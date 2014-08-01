from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Address(models.Model):
    # There's some specific Django fields/libraries for storing location information (State, Zipcode, etc)
    title = models.CharField(max_length=100)
    street = models.CharField(max_length=160, help_text="ex: 225 Maiden Ln")
    city = models.CharField(max_length=160, help_text="ex: San Francisco")
    state = models.CharField(max_length=2,help_text="ex: CA")
    zipcode = models.CharField(max_length=5,help_text="ex: 94019")

    def __unicode__(self):
        return u'{}'.format(self.title)


class Partier(AbstractUser):
    phone = models.CharField(max_length=10, help_text="Format should be: 5551231234")


class Event(models.Model):
    # Not sure what these 'name' attributes are doing, pretty sure they're unnecessary
    title = models.CharField(max_length=40, name='title')
    date = models.CharField(max_length=30, name='date')
    location = models.ForeignKey(Address, name='location')
    creator = models.ForeignKey(Partier, name='creator')
    # Not sure what this field is for, but should it be a number field?
    guest_nums = models.TextField(name='guests', null=True)
