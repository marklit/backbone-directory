# -*- coding: utf-8 -*-
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
import pytz


class City(models.Model):
    name = models.TextField(blank=True)
    
    def __unicode__(self):
        return unicode(self.name)
    
    class Meta:
        verbose_name_plural = _("Cities")
        ordering = ["name"]

class Department(models.Model):
    name = models.TextField(blank=True)
    
    def __unicode__(self):
        return unicode(self.name)
    
    class Meta:
        ordering = ["name"]

class Person(models.Model):
    """
    These are the individual items themselves
    """
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    job_title = models.TextField(blank=True)
    department = models.ForeignKey(Department)
    
    email_address = models.TextField(blank=True)
    office_phone = models.TextField(blank=True)
    mobile_phone = models.TextField(blank=True)
    city = models.ForeignKey(City)
    
    photo_url = models.TextField(blank=True)
    blog_url = models.TextField(blank=True)
    
    created_time = models.DateTimeField(auto_now_add=True,
        default="2000-01-01T01:00:00+00:00")
    hide_person = models.BooleanField(default=False)
    
    def __unicode__(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        full_name = full_name.strip()
        return "%s..." % full_name[:60] if len(full_name) > 60 else full_name
        
    def get_icon_url(self):
        if self.photo_url is not None and \
            len(unicode(self.photo_url).strip()):
            return self.photo_url
        
        return 'http://placehold.it/50x50/ff9900/000000/'
    
    class Meta:
        verbose_name_plural = _("People")
        ordering = ["last_name", "first_name"]