import csv
import re
from pymongo import MongoClient


def read_data(csv_file, db):
    mongo_db = client[db]
    tickets_collection = mongo_db['tickets']

    with open(csv_file, encoding='utf8') as csvfile:
        rows_list = list()
        reader = csv.DictReader(csvfile)

        for row in reader:
            row = dict(row)
            row['Цена'] = int(row['Цена'])
            rows_list.append(row)
        tickets_collection.insert_many(rows_list)

def find_cheapest(db):
    mongo_db = client[db]
    tickets_collection = mongo_db['tickets']

    sorted_list = tickets_collection.find().sort('Цена', 1)
    print(list(sorted_list))

def find_by_name(name, database):в том числе – по подстроке, например "Seconds to"
    mongo_db = client[database]
    tickets_collection = mongo_db['tickets']

    regex = re.compile(name)
    sorted_list = tickets_collection.find({'Исполнитель': regex}).sort('Цена', 1)
    for item in sorted_list:
        print(item)

if __name__ == '__main__':
    client = MongoClient()
    read_data('artists.csv', 'test_db')
    find_cheapest('test_db')
    find_by_name('T', 'test_db')

