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