from indexes import Data, Datom, EAVT
from indexes import AVET, LogIndex
from indexes import EAVT, AEVT


class Transactor:
    def __init__(self):
        self.eavt = EAVT()
        self.aevt = AEVT()
        self.log_index = LogIndex()
        self.t = 0
    
    def insert(self, data):
        try:
            datom = Datom(data.entity, data.attribute, data.value, self.t)
            self.eavt.insert(datom)
            self.aevt.insert(datom)
            self.log_index.insert(datom)
            self.t += 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    db = Transactor()

    db.insert(Data(1, 'name', 'pepe'))
    db.insert(Data(1, 'lastname', 'le Peu'))
    db.insert(Data(1, 'location', 'Santo Domingo'))
    db.insert(Data(2, 'name', 'juan'))
    db.insert(Data(3, 'name', 'ramon'))
    db.insert(Data(4, 'name', 'pedro'))

    print(db.aevt.get("lastname"))
    print(db.eavt.get(1))

    for i in db.log_index.log_index:
        print(i)
