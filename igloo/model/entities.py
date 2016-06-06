# BioDB API
import peewee
import playhouse.postgres_ext
import datetime

from igloo import db


class Software(peewee.Model):
  title = peewee.CharField()
  description = peewee.TextField()
  url = peewee.CharField(null=True)
  license_type = peewee.CharField(null=True)
  reference = peewee.CharField(null=True)
  ftsearch = playhouse.postgres_ext.TSVectorField()

  added = peewee.DateField(default=datetime.datetime.now)

  class Meta:
    database = db

  def save(self, **kwa):
    self.ftsearch = fn.to_tsvector('\n'.join([self.title, self.description]))
    out = super(Software, self).save(**kwa)
    # SoftwareSearch.insert({
    #   SoftwareSearch.docid: self.id,
    #   SoftwareSearch.title: self.title,
    #   SoftwareSearch.description: self.description,
    #   }).execute()
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

