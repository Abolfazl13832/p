from base import BaseClass
VAT={"Iran":9,"UAE":16}
class Purchase(BaseClass):
    def __init__(self, user, address, *args, **kwargs):
        self.user = user
        self.address = address
        self.tool_list = []
        super().__init__(*args, **kwargs)
    def add_tool(self,t_list):
        if not isinstance(t_list,list):
            t_list = [t_list]
        self.tool_list.extend(t_list)
    def total_per_price(self):
        sum = 0
        for tool in self.tool_list:
            sum += tool.rental_price
        return sum
    
def vat_dec(func):
    def wrapped_func(pur):
        total_price = pur.total_per_price()
        vat= VAT[pur.address.country]
        return int(total_price + total_price * vat /100)
    return wrapped_func
@vat_dec
def show_price_plus_vat(p):
    return p.total_per_price()

def show_price(p):
    return p.total_per_price()
    
