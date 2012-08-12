# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('filename', 'width', 'height', 'shutter_speed', 
        'aperture', 'focal_length', 'flash')
    list_filter = ('flash', 'width', 'focal_length',)


admin.site.register(Photo, PhotoAdmin)