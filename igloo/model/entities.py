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
