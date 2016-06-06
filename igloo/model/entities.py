# BioDB API
import peewee
import playhouse.sqlite_ext
import datetime

from igloo import db


class Software(peewee.Model):
  title = peewee.CharField()
  description = peewee.TextField()
  url = peewee.CharField(null=True)
  license_type = peewee.CharField(null=True)
  reference = peewee.CharField(null=True)

  added = peewee.DateField(default=datetime.datetime.now)

  class Meta:
    database = db

  def save(self, **kwa):
    out = super(Software, self).save(**kwa)
    SoftwareSearch.insert({
      SoftwareSearch.docid: self.id,
      SoftwareSearch.title: self.title,
      SoftwareSearch.description: self.description,
      }).execute()
    return out

  @property
  def repr(self):
    return {
      'id': self.id,
      'title': self.title,
      'description': self.description,
      'reference': self.reference,
      'url': self.url,
      'license': self.license_type,
      'added': str(self.added),
    }


class SoftwareSearch(playhouse.sqlite_ext.FTSModel):
  title = playhouse.sqlite_ext.SearchField()
  description = playhouse.sqlite_ext.SearchField()

  class Meta:
    database = db
    extension_options = {'tokenize': 'porter'}


