# BioDB API
import os
import urllib.parse

db_url = urllib.parse.urlsplit(os.environ.get(
    'DATABASE_URL',
    'postgres://prashantsinha:@localhost:5432/biodb'))

db_config = {
  'database': db_url.path[1:],
  'password': db_url.password,
  'user': db_url.username,
  'host': db_url.hostname,
  'port': db_url.port,
  'register_hstore': False,
  'autocommit': True,
  'autorollback': True,
}

module_root = os.getcwd()
static_root = module_root + '/public'
