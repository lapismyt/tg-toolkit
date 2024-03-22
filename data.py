'''
Data storing. Database, datatypes, etc.
'''

# imports
import os
from pickle import dump, load
from datetime import datetime

class BaseModel():
    pass

# database class using pickle
# it can be acessed using database.<param_name> (magic)
# on try to write or read database, use read and write functions
class Database():
    def __init__(self, db_file, autobackup=False):
        # create database file if it doesn't exist
        if not os.path.isfile(db_file):
            self.write(db_file, BaseModel())
        self.db_file = db_file
        self.autobackup = autobackup
        self.ops_to_backup = 10
        self.op_number = 0
    
    # backup func that called on each self.ops_to_backup read/write and places in .backups folder
    def autobackup(self):
        self.op_number += 1
        if self.op_number % self.ops_to_backup == 0:
            self.backup()
    
    # private function read for magic functions
    def read(self):
        db_file = self.db_file
        if self.autobackup:
            self.autobackup(db_file)
        with open(db_file, 'rb') as f:
            return load(f)
    
    # private function write for magic functions
    def write(self, data):
        db_file = self.db_file
        if self.autobackup:
            self.autobackup(db_file)
        with open(db_file, 'wb') as f:
            dump(data, f)
    
    # magic get function
    def __getitem__(self, param_name):
        return self.read(param_name)

    # magic set function
    def __setitem__(self, param_name, param):
        self.write(param_name, param)