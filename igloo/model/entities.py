# BioDB API
import peewee
import datetime

from igloo import db


class Software(peewee.Model):
  title = peewee.CharField()
  description = peewee.TextField()
  url = peewee.CharField(null=True)
  license_type = peewee.CharField(null=True)

  added = peewee.DateField(default=datetime.datetime.now)

  class Meta:
    database = db

  @property
  def repr(self):
    return {
      'id': self.id,
      'title': self.title,
      'description': self.description,
      'url': self.url,
      'license': self.license_type,
      'added': str(self.added),
    }
