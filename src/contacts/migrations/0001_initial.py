# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table('contacts_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('contacts', ['City'])

        # Adding model 'Department'
        db.create_table('contacts_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('contacts', ['Department'])

        # Adding model 'Person'
        db.create_table('contacts_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('last_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('job_title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Department'])),
            ('email_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('office_phone', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mobile_phone', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.City'])),
            ('photo_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('blog_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(default='2000-01-01T01:00:00+00:00', auto_now_add=True, blank=True)),
            ('hide_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('contacts', ['Person'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table('contacts_city')

        # Deleting model 'Department'
        db.delete_table('contacts_department')

        # Deleting model 'Person'
        db.delete_table('contacts_person')


    models = {
        'contacts.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'contacts.department': {
            'Meta': {'object_name': 'Department'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'contacts.person': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'object_name': 'Person'},
            'blog_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.City']"}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'default': "'2000-01-01T01:00:00+00:00'", 'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Department']"}),
            'email_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hide_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'office_phone': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo_url': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['contacts']