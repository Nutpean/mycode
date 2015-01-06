# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class CreditWebtempnew(models.Model):
    temp_id = models.BigIntegerField(primary_key=True)
    filter_status = models.IntegerField(blank=True)
    event_type = models.CharField(max_length=255, blank=True)
    app = models.CharField(max_length=255, blank=True)
    dip = models.CharField(max_length=40, blank=True)
    dport = models.IntegerField(blank=True, null=True)
    sip = models.CharField(max_length=40, blank=True)
    sport = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True)
    file_hash = models.CharField(max_length=500, blank=True)
    file_name = models.CharField(max_length=255, blank=True)
    file_sha = models.CharField(max_length=500, blank=True)
    file_size = models.CharField(max_length=255, blank=True)
    file_type = models.CharField(max_length=255, blank=True)
    info0 = models.CharField(max_length=255, blank=True)
    info1 = models.CharField(max_length=255, blank=True)
    info2 = models.CharField(max_length=255, blank=True)
    info3 = models.CharField(max_length=255, blank=True)
    info4 = models.CharField(max_length=255, blank=True)
    path = models.CharField(max_length=255, blank=True)
    intern_path = models.CharField(max_length=255, blank=True)
    parent_uuid = models.CharField(max_length=255, blank=True)
    parent_file = models.CharField(max_length=255, blank=True)
    parent_hash = models.CharField(max_length=500, blank=True)
    protocol = models.CharField(max_length=255, blank=True)
    uri = models.CharField(max_length=255, blank=True)
    referer = models.CharField(max_length=255, blank=True)
    risk = models.FloatField(blank=True, null=True)
    threat = models.IntegerField(blank=True, null=True)
    threat_path = models.CharField(max_length=255, blank=True)
    create_time = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True)
    av_name = models.CharField(max_length=255, blank=True)
    av_type = models.CharField(max_length=255, blank=True)
    av_accuracy = models.CharField(max_length=255, blank=True)
    detail = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=255, blank=True)
    env = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'credit_webtempnew'
        ordering = ['filter_status']

