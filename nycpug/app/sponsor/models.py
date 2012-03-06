from django.db import models

class Sponsor(models.Model):
    conference = models.ForeignKey('core.Conference', related_name='sponsors')
    category = models.ForeignKey('SponsorCategory', related_name='sponsors')
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sponsors/')
    url = models.URLField(verify_exists=False)
    sort_order = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']

class SponsorCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']
        verbose_name_plural = 'sponsor categories'