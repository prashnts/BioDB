from igloo import db
from igloo.model.entities import Software

if __name__ == '__main__':
  db.drop_tables([Software], safe=True)
  db.create_tables([Software])
