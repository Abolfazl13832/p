from base import BaseClass

class Address(BaseClass):
    def __init__(self, country, *args, **kwargs):
        self.country = country
        super().__init__(*args, **kwargs)