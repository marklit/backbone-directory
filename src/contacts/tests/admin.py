# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client


class ContactsAdminTests(TestCase):
    fixtures = ['contacts']

    def test_admin_pages(self):
        c = Client()
        
        for model_name in ('city', 'department', 'person',):
            for section in ('', '1/', 'add/', '1/history/'):
                result = \
                    c.get('/admin/contacts/%s/%s' % (model_name, section))
                self.assertEqual(result.status_code, 200)
                self.assertTrue(len(result.content.strip()) > 5)