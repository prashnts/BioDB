# BioDB API
import peewee

from igloo import db


class Software(peewee.Model):
  title = peewee.CharField()
  description = peewee.TextField()
  url = peewee.CharField()
  license_type = peewee.CharField()

  added = peewee.DateField()
  updated = peewee.DateField()

  class Meta:
    database = db

