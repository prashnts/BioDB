# BioDB API
import hug
import math

from igloo.model.entities import Software


@hug.get('/')
def get_list(page=1):
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
  item = Software.get(Software.id == uid)
  return item.repr

@hug.post('/')
def add_entity():
  pass

