# BioDB API
import hug
import math
import peewee
import falcon

from igloo.model.entities import Software


@hug.get('/')
def get_list(page: hug.types.number=1):
  items = Software.select().paginate(page, 10)
  pages_count = math.ceil(Software.select().count() / 10)

  return {
    'data': map(lambda x: x.repr, items),
    'paginate': {
      'current_page': page,
      'total_pages': pages_count
    }
  }

@hug.get('/{uid}')
def get_entity(uid: hug.types.text):
  try:
    item = Software.get(Software.id == uid)
    return item.repr
  except peewee.DoesNotExist:
    raise falcon.HTTPNotFound()

@hug.post('/')
def add_entity():
  pass

@hug.put('/{uid}')
def update_entity(uid: hug.types.text):
  pass

@hug.delete('/{uid}')
def delete_entity(uid: hug.types.text):
  pass


