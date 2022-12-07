"""
author: Shiri Yarom
name: database
description: actions for the dictionary
"""

class DataBase:

    def __init__(self):
        """
        init a class that has a dictionary
         """
        self.dict = {None: None}

    def set_value(self, key, val):
        """
                changes the value of the value of the key in the dictionary
                :param key
                :param val
                :return: True/ False if it works
                """
        self.dict.update({key: val})
        return True

    def get_value(self, key):
        """
               returns the value of the value of the key in the dictionary
               :param key
               :return: the value of the value of the key's dictionary
               """
        if key in self.dict.keys():
            return self.dict[key]
        return None

    def delete_value(self, key):
        """
              deletes the value of the value of the key in the dictionary
              :param key
              :return: the value that was deleted
              """
        if key in self.dict.keys():
            return self.dict.pop(key)
        return None

