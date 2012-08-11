# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from contacts.api import PersonResource


v1_api = Api(api_name="v1")

v1_api.register(PersonResource())

urlpatterns = patterns("",
    url("", include(include(v1_api.urls))),
)