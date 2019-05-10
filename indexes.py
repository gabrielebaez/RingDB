from abc import ABC, abstractmethod
from collections import namedtuple

Data = namedtuple('Data', ['entity', 'attribute', 'value'])
Datom = namedtuple('Datom', ['entity', 'attribute', 'value', 'tx'])


class BaseIndex(ABC):

    @abstractmethod
    def insert(self, datom):
        pass
    
    @abstractmethod
    def get(self, key):
        pass


class EAVT(BaseIndex):
    def __init__(self):
        self.EAVT_index = {}
    
    def insert(self, datom):
        key = datom.entity

        if key in self.EAVT_index:
            self.EAVT_index[key][datom.attribute] = [datom.value, datom.tx]
        else:
            self.EAVT_index[key] = {}
            self.EAVT_index[key][datom.attribute] = [datom.value, datom.tx]

    def get(self, key):
        try:
            return self.EAVT_index[key]
        except Exception as e:
            raise e

class AEVT:
    def __init__(self):
        self.AEVT_index = {}
    
    def insert(self, datom):
        key = datom.attribute

        if key in self.AEVT_index:
            self.AEVT_index[key][datom.entity] = [datom.value, datom.tx]
        else:
            self.AEVT_index[key] = {}
            self.AEVT_index[key][datom.entity] = [datom.value, datom.tx]
   
    def get(self, key):
        try:
            return self.AEVT_index[key]
        except Exception as e:
            raise e


class VAET:
    pass


class AVET:
    pass


class LogIndex:
    def __init__(self):
        self.log_index = []
    
    def insert(self, datom):
        self.log_index.append(datom)
