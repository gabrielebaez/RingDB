from transactor import Transactor, Data


db = Transactor()

db.create_entity('user', {'user/name': 'pepe',
                            'city/name': 'santo domingo',
                            'follows': 'candace'})

db.create_entity('user', {'user/name': 'candace',
                            'city/name': 'santo domingo',
                            'follows': 'pepe'}) 

# db.insert(Data('JC', 'Lives in', 'Rome'))
# db.insert(Data('B', 'Lives in', 'Rome'))
# db.insert(Data('JC', 'Died in', 'Rome'))
# db.insert(Data('Cleo', 'Lives in', 'Egypt'))
# db.insert(Data('Rome', 'river', 'Tiber'))
# db.insert(Data('Egypt', 'river', 'Nile'))

# db.insert(Data(0, 'extra', 'more data'))
# db.insert(Data(0, 'extra', 'even more data')) 


print("EAVT: ")
print(db.eavt.EAVT_index)
print("------")
print("AEVT: ")
print(db.aevt.AEVT_index)
print("------")
print("VAET: ")
print(db.vaet.VAET_index)
