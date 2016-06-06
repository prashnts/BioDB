import csv

from igloo import db
from igloo.model.entities import Software, SoftwareSearch

def populate_db():
  with open('data/sample.data.csv', 'r') as fl:
    rows = csv.DictReader(fl)
    for row in rows:
      item = Software()
      item.title = row.get('Software Name')
      item.description = row.get('One line discription')
      item.url = row.get('Software link')
      item.reference = row.get('Reference (journel or publication name)')
      item.save()

if __name__ == '__main__':
  db.drop_tables([Software, SoftwareSearch], safe=True)
  db.create_tables([Software])
  SoftwareSearch.create_table()
  populate_db()
  print("Done Create DB")
