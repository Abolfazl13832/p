from user import User
from store import Store
from tools import ConstructionPile, Drill, BaseTool
from vendor import Vendor
from purchase import Purchase ,show_price_plus_vat ,show_price
from address import Address

VAT={"Iran":9,"UAE":16}
CONTRIES=list(VAT.keys())
s= Store(name="my tools",
         shop_contact_number="04532539281",
         address="Parvaneh Street",
         area="Terminal",
         vendor=Vendor(frist_name="Abolfazl", last_name="alipour" ,phone_number="09929399646", is_licensed=True),
         tool_list = BaseTool.object_list)
c1 = ConstructionPile('c1',2,'150',10000,)
c2 = ConstructionPile('c2',2.5,'150',15000,)
c3 = ConstructionPile('c3',3,'150',20000,)
c4 = ConstructionPile('c4',3.5,'150',25000,)
d1=Drill(name='d1',rental_price = 100000,quantity=2,type='t1',mark='m1')
d2=Drill(name='d2',rental_price=200000,quantity=2,type='t2',mark='m2')
d3=Drill(name='d3',rental_price=150000,quantity=2,type='t3',mark='m3')
d4=Drill(name='d4',rental_price=300000,quantity=2,type='t4',mark='m4')
user=User()
address_iran = Address(country=CONTRIES[0])
address_uae = Address(country=CONTRIES[1])
purchase = Purchase(user=user,address=address_iran)
purchase.add_tool(c1)
purchase.add_tool([c2,c3,c4,d1,d2,d3,d4])


sh= show_price_plus_vat(purchase)

print(sh)
print(show_price(purchase))




    