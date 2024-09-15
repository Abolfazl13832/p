from abc import ABC
class BaseClass(ABC):
    _id = 0
    object_list = None
    def __init__(self,*args,**kwargs):
        self.id =self.generate_id()
        self.object_list = self.create_object(self)
        super().__init__(*args,**kwargs)
    
    @classmethod
    def generate_id(cls):
        cls._id+=1
        return cls._id

    @classmethod
    def create_object(cls,object):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(object)
