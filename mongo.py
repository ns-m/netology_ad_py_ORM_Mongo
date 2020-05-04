import csv
import re
import pprint
from datetime import datetime
from pymongo import MongoClient


def connection(database):
    client = MongoClient()
    db = client[database]
    collection = db['concert']
    return collection

