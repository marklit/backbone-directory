# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
import json


class ContactsAdminTests(TestCase):
    fixtures = ['contacts']

    def test_all_people(self):
        c = Client()
        result = c.get('/api/v1/person/?format=json')
        self.assertEqual(result.status_code, 200)
        
        response = json.loads(result.content)
        
        expected_meta = {
            u'previous': None, 
            u'total_count': 1, 
            u'offset': 0, 
            u'limit': 20, 
            u'next': None
        }
        expected_objects = \
            [{"first_name": "Mark", "last_name": "Litwintschik"}]
        
        self.assertEqual(len(set(expected_meta) - set(response['meta'])), 0)
        
        for (k, v) in response['meta'].items():
            self.assertTrue(expected_meta[k] is v)
        
        self.assertEqual(len(response['objects']), 1)
        
        for key in ('first_name', 'last_name'):
            self.assertEqual(response['objects'][0][key], 
                                expected_objects[0][key])
    
    def test_no_results(self):
        c = Client()
        result = c.get('/api/v1/person/?format=json&id=2')
        self.assertEqual(result.status_code, 200)
        
        response = json.loads(result.content)
        self.assertEqual(response['meta']['total_count'], 0)