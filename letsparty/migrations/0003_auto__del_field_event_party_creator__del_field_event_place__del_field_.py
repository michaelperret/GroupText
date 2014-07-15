# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.party_creator'
        db.delete_column(u'letsparty_event', 'party_creator_id')

        # Deleting field 'Event.place'
        db.delete_column(u'letsparty_event', 'place_id')

        # Deleting field 'Event.data'
        db.delete_column(u'letsparty_event', 'data')

        # Adding field 'Event.date'
        db.add_column(u'letsparty_event', 'date',
                      self.gf('django.db.models.fields.CharField')(default='6/10/14', max_length=30),
                      keep_default=False)

        # Adding field 'Event.location'
        db.add_column(u'letsparty_event', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['letsparty.Address']),
                      keep_default=False)

        # Adding field 'Event.creator'
        db.add_column(u'letsparty_event', 'creator',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['letsparty.Partier']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Event.party_creator'
        raise RuntimeError("Cannot reverse this migration. 'Event.party_creator' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.party_creator'
        db.add_column(u'letsparty_event', 'party_creator',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['letsparty.Partier']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Event.place'
        raise RuntimeError("Cannot reverse this migration. 'Event.place' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.place'
        db.add_column(u'letsparty_event', 'place',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['letsparty.Address']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Event.data'
        raise RuntimeError("Cannot reverse this migration. 'Event.data' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.data'
        db.add_column(u'letsparty_event', 'data',
                      self.gf('django.db.models.fields.DateField')(),
                      keep_default=False)

        # Deleting field 'Event.date'
        db.delete_column(u'letsparty_event', 'date')

        # Deleting field 'Event.location'
        db.delete_column(u'letsparty_event', 'location_id')

        # Deleting field 'Event.creator'
        db.delete_column(u'letsparty_event', 'creator_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'letsparty.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'letsparty.event': {
            'Meta': {'object_name': 'Event'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['letsparty.Partier']"}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['letsparty.Address']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'letsparty.partier': {
            'Meta': {'object_name': 'Partier'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['letsparty']