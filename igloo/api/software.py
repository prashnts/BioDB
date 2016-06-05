# BioDB API
import hug
import math
import peewee
import falcon

from igloo.model.entities import Software


@hug.get('/')
def get_list(
    page: hug.types.number=1,
    q: hug.types.text=None):
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
def add_entity(
    title: hug.types.text,
    description: hug.types.text,
    url: hug.types.text=None,
    license: hug.types.text=None):
  try:
    new_item = Software()
    new_item.title = title
    new_item.description = description
    new_item.url = url
    new_item.license_type = license
    new_item.save()
  except peewee.IntegrityError as e:
    raise falcon.HTTPMissingParam(param_name=str(e))
  else:
    return new_item.repr

@hug.put('/{uid}')
def update_entity(
    uid: hug.types.text,
    title: hug.types.text=None,
    description: hug.types.text=None,
    url: hug.types.text=None,
    license: hug.types.text=None):
  kwas = locals()
  del kwas['uid']
  try:
    item = Software.get(Software.id == uid)
  except peewee.DoesNotExist:
    raise falcon.HTTPNotFound
  else:
    updates = []
    for key, val in kwas.items():
      if val is not None:
        setattr(item, key, val)
        updates.append(key)
    try:
      item.save()
    except peewee.IntegrityError as e:
      raise falcon.HTTPBadRequest(
        title='Validation Error',
        description=str(e))
    else:
      return item.repr

@hug.delete('/{uid}')
def delete_entity(uid: hug.types.text):
  try:
    item = Software.get(Software.id == uid)
  except peewee.DoesNotExist:
    raise falcon.HTTPNotFound
  else:
    item.delete_instance()
    return item.repr
