# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stock.ticker'
        db.add_column(u'stocks_stock', 'ticker',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=6),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stock.ticker'
        db.delete_column(u'stocks_stock', 'ticker')


    models = {
        u'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['stocks']