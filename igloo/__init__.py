# BioDB API
import hug
import pecan_mount
import static

import igloo._config as config

import playhouse.postgres_ext

db = playhouse.postgres_ext.PostgresqlExtDatabase(**config.db_config)


@hug.get('/')
def get_root():
  return 'Go to /api/docs for docs'


from igloo.api import software as api_software

@hug.extend_api('/software')
def attach_software_api():
  return [api_software]


# Get WSGI friendly environment for *both* Static Files and API
pecan_mount.tree.graft(__hug_wsgi__, '/api')
pecan_mount.tree.graft(static.Cling(config.static_root), '/')

api = pecan_mount.tree
