# BioDB API
import hug

import igloo._config as config

from peewee import SqliteDatabase

db = SqliteDatabase(config.db_name)


@hug.get('/')
def get_root():
  return 'Hello World.'


