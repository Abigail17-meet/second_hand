from model import *


#Make new Users

lorenzo = Customer(name="Lorenzo", email = "lobrown@meet.mit.edu", address = "Moshe Hess 7")
lorenzo.hash_password("myPassword")
session.add(lorenzo)
session.commit()


Abigail = Customer(name="Abigail", email = "gugigil@gmail.com", address = "Hashkedim 10")
Abigail.hash_password("myPassword")
session.add(Abigail)
session.commit()

Uria = Customer(name="Uria", email = "uria@gmail.com", address = "Galil 19")
Uria.hash_password("myPassword")
session.add(Uria)
session.commit()

Jana = Customer(name="Jana", email = "jana@meet.mit.edu", address = "derech hayam")
Jana.hash_password("myPassword")
session.add(Jana)
session.commit()

#Make Items

item1 = Item(description = "putsomething here", price = "99", picture = "", location = "Tivon")
item1.customer_id = 1
session.add(item1)
session.commit()

item2 = Item(description = "apple", price = "9", picture= "", location = "Nazareth")
item2.customer_id = 4
session.add(item2)
session.commit()

item3 = Item(description = "apple", price = "12", picture = "", location = "Tel-Aviv")
item3.customer_id = 3
session.add(item3)
session.commit()



#Make Comments
comment1 = Comment(text="yummy") 
comment1.customer_id=1
comment1.item_id=1
session.add(comment1)
session.commit()

comment2 = Comment(text="ewww") 
comment2.customer_id=4
comment2.item_id=2
session.add(comment2)
session.commit()

comment3 = Comment(text="I would never buy it!") 
comment3.customer_id=4
comment3.item_id=3
session.add(comment3)
session.commit()