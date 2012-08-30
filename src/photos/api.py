# -*- coding: utf-8 -*-
from haystack.query import SearchQuerySet
from .models import Photo
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.throttle import BaseThrottle


class CameraSettingResource(ModelResource):
    class Meta:
        allowed_methods = ["get"]
        cache = SimpleCache()
        fields = ["id", "aperture", "shutter_speed"]
        include_resource_uri = False
        queryset = Photo.objects.filter(aperture__gt=0, shutter_speed__gt=0)
        resource_name = "camera_settings"
        #authentication = BasicAuthentication()
        #authorization = DjangoAuthorization()
        throttle = \
            BaseThrottle(throttle_at=100, timeframe=3600, expiration=604800)
        filtering = {
            'id': ALL,
            'aperture': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'shutter_speed': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
    
    # def dehydrate(self, bundle):
    #     bundle.data['avatar_icon'] = bundle.obj.get_icon_url()
    #     return bundle