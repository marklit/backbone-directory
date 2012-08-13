# -*- coding: utf-8 -*-
from contacts.api import PersonResource
from django.conf.urls import patterns, include, url
from photos.api import CameraSettingResource
from tastypie.api import Api


v1_api = Api(api_name="v1")

v1_api.register(CameraSettingResource())
v1_api.register(PersonResource())

urlpatterns = patterns("",
    url("", include(include(v1_api.urls))),
)