"""
author: Shiri Yarom
name: SynDataBase
description: sync of the readers and the writters
so they would have te accsses by the right rules
"""

import threading
import multiprocessing
from filedatabase import FileDatabase


class SynDataBase():

    def init(self, mode, database):
        """
              init class that sync between readers and writers
              :param mode: threading/ processing
              :param database
              """
        super().init()
        self.mode = mode
        self.database = database
        if self.mode == 'threading':
            self.lock = threading.Lock()
            self.semaphore = threading.Semaphore(10)
        if self.mode == 'processing':
            self.lock = multiprocessing.Lock()
            self.semaphore = multiprocessing.Semaphore(10)

    def write_data(self):
        """
              have the accseed to changes values in the dictionary
              :return: None
              """
        self.lock.acquire()
        for k in range(10):
            self.semaphore.acquire()

    def write_release(self):
        """
               release access to change values in the dictionary
               :return: None
               """
        for k in range(10):
            self.semaphore.release()
        self.lock.release()

    def get_value(self, key):
        """
                returns in the dictionary the value of the value before of
                the key
                :param key
                :return: flag - the value of the value of the key's dictionary
                """
        self.semaphore.acquire()
        value = self.database.get_value(key)
        self.semaphore.release()
        return value

    def set_value(self, key, val):
        """
             changes in the dictionary the value of the value before of
             the key
             :param key
             :param val
             :return: flag - True/ False if it works
             """
        self.lock.acquire()
        for k in range(10):
            self.semaphore.acquire()
        flag = self.database.set_value(key, val)
        self.lock.release()
        for k in range(10):
            self.semaphore.release()
        return flag

    def delete_value(self, key):
        """
                    deletes in the dictionary the value of the value before of
                     the key
                     :param key
                     :param val
                     :return: flag - True/ False if it works
                     """
        self.write_data()
        flag = self.database.delete_value(key)
        self.write_release()
        return flag


    def reader_db(database):
        """
        reader is trying to get an access to read
        the value from the dictionary
        :param database
        :return: None
        """
        print("reader started")
        for k in range(100):
            flag = database.get_value(k) == k or database.get_value(k) is None
            assert flag
        print("reader left")

    def writer_db(database):
        """
        writer is trying to get an access to write the
        value from the dictionary
        :param database
        :return: None
        """
        print("writer has accsess")
        for k in range(100):
            assert database.set_value(k, k)
        for k in range(100):
            flag = database.delete_value(k) == k or database.delete_value(k) is None
            assert flag
        print("writer is gone")

