from abc import ABC
class BaseTool(ABC):
    _id = 0
    object_list=None
    total_list = list()
    def __init__(self, name, quantity, rental_price, *args, **kwargs):
        self.id =self.generate_id()
        self.object_list = self.create_object(self)
        self.name = name
        self.quantity = quantity
        self.rental_price = rental_price
        super().__init__(*args, **kwargs)
        
    @classmethod
    def generate_id(cls):
        cls._id+=1
        return cls._id

    @classmethod
    def create_object(cls,object):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(object)
        cls.total_list.append(object)


class Drill(BaseTool):
    def __init__(self, name, rental_price, quantity, type, mark,  *args, **kwargs):
        self.type = type
        self.mark = mark
        super().__init__(name, quantity, rental_price, *args, **kwargs)



class ConstructionPile(BaseTool):
    def __init__(self, name,size, quantity, rental_price, *args, **kwargs):
        self.size = size
        super().__init__(name, quantity, rental_price, *args, **kwargs)
    def show_d(self):
        m=f"****************\n{self.name}\n{self.quantity}**************"
        return m


