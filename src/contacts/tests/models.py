# -*- coding: utf-8 -*-
from django.test import TestCase
from contacts.models import City, Department, Person

class ContactsModelsTests(TestCase):
    fixtures = ['contacts']
        
    def test_city(self):
        pass
    
    def test_department(self):
        pass
    
    def test_person(self):
        people = Person.objects.all()
        self.assertTrue(len(people) > 0)
        self.assertEqual(people[0].first_name, u'Mark')