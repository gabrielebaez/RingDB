from abc import ABC, abstractmethod
from collections import namedtuple
from unqlite import UnQLite

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
        # self.EAVT_index = {}
        self.EAVT_index = UnQLite()
    
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


class SimpleTransactor:

    def __init__(self):
        self.eavt = EAVT()
        self.tx = 0
    
    def insert(self, data):
        datom = Datom(data.entity, data.attribute, data.value, self.tx)
        self.eavt.insert(datom)
        self.tx += 1


if __name__ == "__main__":

    t = SimpleTransactor()
    print(t.eavt.EAVT_index)

    t.insert(Data('JC', 'Lives in', 'Rome'))
    print(t.eavt.EAVT_index)

    t.insert(Data('JC', 'music', 'tame'))
    print(t.eavt.EAVT_index)
