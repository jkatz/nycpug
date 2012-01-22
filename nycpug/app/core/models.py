from django.db import models

class Conference(models.Model):
    """
        set name and other info for conference
    """
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)

    sponsor_categories = models.ManyToManyField('sponsor.SponsorCategory')

    def __unicode__(self):
        return self.name

class Venue(models.Model):
    """
        set venue information for a conference
    """
    conference = models.OneToOneField('Conference', blank=True)
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=2)
    description = models.TextField()