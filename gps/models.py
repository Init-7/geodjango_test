#from __future__ import unicode_literals
#from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


#class Databasechangelog(models.Model):
#    id = models.CharField(max_length=255)
#    author = models.CharField(max_length=255)
#    filename = models.CharField(max_length=255)
#    dateexecuted = models.DateTimeField()
#    orderexecuted = models.IntegerField()
#    exectype = models.CharField(max_length=10)
#    md5sum = models.CharField(max_length=35, blank=True, null=True)
#    description = models.CharField(max_length=255, blank=True, null=True)
#    comments = models.CharField(max_length=255, blank=True, null=True)
#    tag = models.CharField(max_length=255, blank=True, null=True)
#    liquibase = models.CharField(max_length=20, blank=True, null=True)
#    contexts = models.CharField(max_length=255, blank=True, null=True)
#    labels = models.CharField(max_length=255, blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'databasechangelog'
#

class Databasechangeloglock(models.Model):
    id = models.IntegerField(primary_key=True)
    locked = models.BooleanField()
    lockgranted = models.DateTimeField(blank=True, null=True)
    lockedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databasechangeloglock'


class Devices(models.Model):
    name = models.CharField(max_length=128)
    uniqueid = models.CharField(db_column='uniqueId', unique=True, max_length=128)  # Field name made lowercase.
    status = models.CharField(max_length=128, blank=True, null=True)
    lastupdate = models.DateTimeField(db_column='lastUpdate', blank=True, null=True)  # Field name made lowercase.
    positionid = models.IntegerField(db_column='positionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'devices'
    def __unicode__(self):
        return u"%s %s" % (self.id, self.uniqueid)


#class Layer(models.Model):
#    topology = models.ForeignKey('Topology', models.DO_NOTHING)
#    layer_id = models.IntegerField()
#    schema_name = models.CharField(max_length=-1)
#    table_name = models.CharField(max_length=-1)
#    feature_column = models.CharField(max_length=-1)
#    feature_type = models.IntegerField()
#    level = models.IntegerField()
#    child_id = models.IntegerField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'layer'
#        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class Positions(models.Model):
#    protocol = models.CharField(max_length=128, blank=True, null=True)
    deviceid = models.ForeignKey(Devices, models.DO_NOTHING, db_column='deviceId')  # Field name made lowercase.
#    servertime = models.DateTimeField(db_column='serverTime')  # Field name made lowercase.
    devicetime = models.DateTimeField(db_column='deviceTime')  # Field name made lowercase.
#    fixtime = models.DateTimeField(db_column='fixTime')  # Field name made lowercase.
    valid = models.BooleanField()
    lat = models.FloatField()
    lon = models.FloatField()
#    altitude = models.FloatField()
#    speed = models.FloatField()
#    course = models.FloatField()
    address = models.CharField(max_length=512, blank=True, null=True)
    attributes = models.CharField(max_length=4096)
    geom = models.PointField(db_column='punto', srid=4326, default='SRID=4326;POINT(0.0 0.0)')
#    objects = models.GeoManager()

    class Meta:
        managed = True
        db_table = 'pos'

    def __unicode__(self):
        return u"%s %s %s %s" % (self.id, self.deviceid, self.lat, self.lon)


#class Positions(models.Model):
#    protocol = models.CharField(max_length=128, blank=True, null=True)
#    deviceid = models.ForeignKey(Devices, models.DO_NOTHING, db_column='deviceId')  # Field name made lowercase.
#    servertime = models.DateTimeField(db_column='serverTime')  # Field name made lowercase.
#    devicetime = models.DateTimeField(db_column='deviceTime')  # Field name made lowercase.
#    fixtime = models.DateTimeField(db_column='fixTime')  # Field name made lowercase.
#    valid = models.BooleanField()
#    latitude = models.FloatField()
#    longitude = models.FloatField()
#    altitude = models.FloatField()
#    speed = models.FloatField()
#    course = models.FloatField()
#    address = models.CharField(max_length=512, blank=True, null=True)
#    attributes = models.CharField(max_length=4096)
#    point = models.PointField(srid=4326, default='SRID=4326;POINT(0.0 0.0)')
##    objects = models.GeoManager()
#
#    class Meta:
#        managed = True
#        db_table = 'positions'
#
#    def save(self, *args, **kargs):
#        self.point.x = self.longitude
#        self.point.y = self.latitude
#        super(Positions, self).save(*args,**kargs)
#
#    def __unicode__(self):
#        return u"%s %s %s %s" % (self.id, self.deviceid, self.latitude, self.longitude)


class Server(models.Model):
    registration = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    map = models.CharField(max_length=128, blank=True, null=True)
    language = models.CharField(max_length=128, blank=True, null=True)
    distanceunit = models.CharField(db_column='distanceUnit', max_length=128, blank=True, null=True)  # Field name made lowercase.
    speedunit = models.CharField(db_column='speedUnit', max_length=128, blank=True, null=True)  # Field name made lowercase.
    bingkey = models.CharField(db_column='bingKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    mapurl = models.CharField(db_column='mapUrl', max_length=128, blank=True, null=True)  # Field name made lowercase.
    readonly = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'server'


#class Topology(models.Model):
#    name = models.CharField(unique=True, max_length=-1)
#    srid = models.IntegerField()
#    precision = models.FloatField()
#    hasz = models.BooleanField()
#
#    class Meta:
#        managed = False
#        db_table = 'topology'


class UserDevice(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    deviceid = models.ForeignKey(Devices, models.DO_NOTHING, db_column='deviceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_device'


class Users(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(unique=True, max_length=128)
    hashedpassword = models.CharField(db_column='hashedPassword', max_length=128)  # Field name made lowercase.
    salt = models.CharField(max_length=128)
    readonly = models.BooleanField()
    admin = models.BooleanField()
    map = models.CharField(max_length=128, blank=True, null=True)
    language = models.CharField(max_length=128, blank=True, null=True)
    distanceunit = models.CharField(db_column='distanceUnit', max_length=128, blank=True, null=True)  # Field name made lowercase.
    speedunit = models.CharField(db_column='speedUnit', max_length=128, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'

