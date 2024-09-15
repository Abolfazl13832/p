from store import Store
from tools import ConstructionPile, Drill, BaseTool
from vendor import Vendor


c1 = ConstructionPile('a','2','3',40000,)
c2 = ConstructionPile('b','2','3',40000,)
c3 = ConstructionPile('c','2','3',40000,)
c4 = ConstructionPile('d','2','3',40000,)
d1=Drill('d',10000,5,'a','sa')
d1=Drill('d',10000,5,'a','sa')
d1=Drill('d',10000,5,'a','sa')
d1=Drill('d',10000,5,'a','sa')

s= Store(name="my tools",
         shop_contact_number="04532539281",
         address="Parvaneh Street",
         area="Terminal",
         vendor=Vendor(frist_name="Abolfazl", last_name="alipour" ,phone_number="09929399646", is_licensed=True),
         tool_list = BaseTool.object_list)

s.show_detail()
print(Store.show_tools(BaseTool.total_list))


    