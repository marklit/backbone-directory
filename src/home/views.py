# -*- coding: utf-8 -*-
from base.utils import json_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('home/home.html', {}, 
        context_instance=RequestContext(request))


@json_response
def login_user(request):
    # @todo Change GET to POST as soon as you can
    user = authenticate(username=request.POST.get('username', ''), 
        password=request.POST.get('password', ''))
    
    if user is None:
        return {'login_successful': False, 'reason': 'Account not found'}
    
    login(request, user)
    
    if user is not None:
        if user.is_active:
            return {'login_successful': True}
            
        return {'login_successful': False, 'reason': 'Account Disabled'}
    
    return {'login_successful': False, 'reason': 'Account not found'}
