from __future__ import unicode_literals

from django.db import models
from authentication.models import Account

import us

#Venue profile information to include:
#   name
#   date range (for temp venues)
#   Location
#   Description
#   Media content (if available)
#   Sport type
#   Age range

class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(Account)
    description = models.TextField()

    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    street = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=40, blank=True)
    STATES = us.states.STATES
    STATE_CHOICES = []
    for STATE in STATES:
        STATE_CHOICES.append( (str(STATE.abbr), str(STATE.name)) )
    STATE_CHOICES = tuple(STATE_CHOICES)
    state = models.CharField(max_length=2,
                             choices=STATE_CHOICES,
                             blank=True
    )
    zipcode = models.CharField(max_length=5) #TODO:need to validate that it is exactly 5

    #TODO: media content field

    sport = models.CharField(max_length=40, blank=True)
