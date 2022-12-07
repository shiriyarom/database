"""
author: Shiri Yarom
name: threading
description: it checks the sync of writers and readers while
mode is threading
"""

from database import DataBase
from filedatabase import FileDataBase
from syndatabase import SynDataBase
from threading import Thread
import logging

Fname = "newfile"
mode = "threading"


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

def main():
    """
         running of the writers and the readers while combine
          them togheter by using threading
        :return: None
        """

    logging.basicConfig(filename='logging_thread.text',
      level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
    data = SynDataBase(mode, FileDataBase(Fname))
    SynDataBase.write_db(data)
    SynDataBase.read_db(data)
    # הרשאת כתיבה כאשר יש תחרות
    print(" other process running  ")
    all_threads = []
    for k in range(0, 10):
        thread = Thread(target=SynDataBase.reader_db, args=(data, ))
        all_threads.append(thread)
        thread.start()
    for k in all_threads:
        k.join()
    for k in range(0, 50):
        thread = Thread(target=SynDataBase.writer_db, args=(data, ))
        all_threads.append(thread)
        thread.start()
    for k in all_threads:
        k.join()


if __name__ == "main":
  main()
