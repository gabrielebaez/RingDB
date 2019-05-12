from indexes import Data, Datom, EAVT
from indexes import AVET, LogIndex
from indexes import EAVT, AEVT
from indexes import VAET, AVET


class Transactor:
    def __init__(self):
        self.eavt = EAVT()
        self.aevt = AEVT()
        self.vaet = VAET()
        self.log_index = LogIndex()
        self.t = 0
    
    def insert(self, data):
        try:
            datom = Datom(data.entity, data.attribute, data.value, self.t)
            self.eavt.insert(datom)
            self.aevt.insert(datom)
            self.vaet.insert(datom)
            self.log_index.insert(datom)
            self.t += 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    db = Transactor()

    db.insert(Data('JC', 'Lives in', 'Rome'))
    db.insert(Data('B', 'Lives in', 'Rome'))
    db.insert(Data('Cleo', 'Lives in', 'Egypt'))
    db.insert(Data('Rome', 'river', 'Tiber'))
    db.insert(Data('Egypt', 'river', 'Nile'))

    print("AEVT: ")
    print(db.aevt.AEVT_index)
    print("------")
    print("EAVT: ")
    print(db.eavt.EAVT_index)
    print("------")
    print("VAET: ")
    print(db.vaet.VAET_index)

    for i in db.log_index.log_index:
        print(i)
