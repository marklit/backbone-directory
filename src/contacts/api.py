# -*- coding: utf-8 -*-
from haystack.query import SearchQuerySet
from .models import Person
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource
from tastypie.throttle import BaseThrottle


class PersonResource(ModelResource):
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
    
        orm_filters = super(PersonResource, self).build_filters(filters)
    
        if "q" in filters:
            orm_filters["pk__in"] = \
                [i.pk for i in SearchQuerySet().auto_query(filters['q'])]
    
        return orm_filters
        
    class Meta:
        allowed_methods = ["get"]
        cache = SimpleCache()
        fields = ["first_name", "last_name"]
        include_resource_uri = False
        queryset = Person.objects.all()
        resource_name = "person"
        #authentication = BasicAuthentication()
        #authorization = DjangoAuthorization()
        throttle = \
            BaseThrottle(throttle_at=100, timeframe=3600, expiration=604800)