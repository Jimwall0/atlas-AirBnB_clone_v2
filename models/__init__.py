#!/usr/bin/python3
"""Storage initialization"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

# Switch between DBStorage and FileStorage depending on environment variable
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
