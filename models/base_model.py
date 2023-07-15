#!/usr/bin/python3
"""
base_model module, it has class BaseModel
which  defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    and handles serialization, deserialization
    """

    def __init__(self, *args, **kwargs):
        """ constructor initalize with id, create/update time
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(val))
                elif key != '__class__':
                    setattr(self, key, val)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            curtime = datetime.now()
            self.created_at = curtime
            self.updated_at = curtime
            storage.new(self)

    def __str__(self):
        """ str representation of object instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """ turn object into dictionary
        """
        dic = self.__dict__
        result_dic = {'__class__': self.__class__.__name__}
        for key, val in dic.items():
            result_dic[key] = val
        result_dic['created_at'] = result_dic['created_at'].isoformat()
        result_dic['updated_at'] = result_dic['updated_at'].isoformat()
        return result_dic

    def save(self):
        """save the object instance
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
