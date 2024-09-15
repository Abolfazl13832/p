from base import BaseClass


class Vendor(BaseClass):
    def __init__(self, frist_name, last_name, phone_number, is_licensed, *args, **kwargs):
        self.frist_name = frist_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.is_licensed = is_licensed
        super().__init__(*args, **kwargs)