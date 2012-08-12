# -*- coding: utf-8 -*-
from django.db import models


class Photo(models.Model):
    filename = models.TextField(blank=True)
    width = models.IntegerField(default=0, null=True)
    height = models.IntegerField(default=0, null=True)
    shutter_speed = models.FloatField(default=0.0, null=True)
    aperture = models.FloatField(default=0.0, null=True)
    focal_length = models.IntegerField(default=0, null=True)
    flash = models.BooleanField(default=False)

    
    def __unicode__(self):
        if len(self.filename) > 60:
            return "%s..." % self.filename[:60]
        return self.filename