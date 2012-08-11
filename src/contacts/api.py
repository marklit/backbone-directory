# -*- coding: utf-8 -*-
from haystack.query import SearchQuerySet
from .models import Person
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
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
        fields = ["id", "first_name", "last_name", "job_title", "blog_url",
            "email_address", "mobile_phone", "office_phone"]
        include_resource_uri = False
        queryset = Person.objects.filter(hide_person=False)
        resource_name = "person"
        #authentication = BasicAuthentication()
        #authorization = DjangoAuthorization()
        throttle = \
            BaseThrottle(throttle_at=100, timeframe=3600, expiration=604800)
        filtering = {
            'id': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'first_name': ['exact', 'startswith', 'endswith', 'contains'],
            'created_time': ALL,
        }
    
    def dehydrate(self, bundle):
        bundle.data['avatar_icon'] = bundle.obj.get_icon_url()
        return bundle