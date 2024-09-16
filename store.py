from base import BaseClass

class Store(BaseClass):
    def __init__(self,name,shop_contact_number,address,area, vendor, tool_list = list , *args , **kwargs):
        self.name = name
        self.shop_contact_number = shop_contact_number
        self.address = address
        self.area = area 
        self.vendor = vendor
        self.tool_list = tool_list
        super().__init__(*args,**kwargs)

    def show_tools(tool_list):
        message =str()
        for i in tool_list:
            message +=f""" 
                        name\tquantity\trental price
                        {i.name}\t{i.quantity}\t\t{i.rental_price}  """
        return message
    def show_detail(self):
        message = f"*****SHOP INFORMATION*****\nshop name : {self.name}\nshop contact number : {self.shop_contact_number}\narea : {self.area}\naddress : {self.address}\n*****VENDOR INFORMATION*****\nname : {self.vendor.frist_name} {self.vendor.last_name}\nphone number : {self.vendor.phone_number}\nis licensed : {self.vendor.is_licensed}\n*****TOOL LIST*****\n"
        print(message)



