# -*- coding: utf-8 -*-
from base.utils import json_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def home(request):
    with open("../frontend/index.html", 'r') as f:
        html = f.read()
    return HttpResponse(html)


@json_response
def login_user(request):
    user = authenticate(username=request.POST.get('username', ''), 
                        password=request.POST.get('password', ''))
    
    if user is None:
        return {'login_successful': False, 'reason': 'Account not found'}
    
    login(request, user)
    
    if user is not None:
        if user.is_active:
            return {'login_successful': True}
            
        return {'login_successful': False, 'reason': 'Account disabled'}
    
    return {'login_successful': False, 'reason': 'Account not found'}
