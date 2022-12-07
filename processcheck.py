"""
author: Shiri Yarom
name: proccess
description: it checks the sync of writers and readers while
mode is processing
"""

from filedatabase import FileDatabase
from syndatabase import SynDataBase
from multiprocessing import Process
import logging


Fname = "new_file"
mode = 'processing'


def main():
    """
     running of the writers and the readers while combine
      then togheter by using multiprocessing
    :return: None
    """
    logging.basicConfig(filename='logging_process.text', level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
    data = SynDataBase(mode, FileDatabase(Fname))
    print(" no other process ")
    SynDataBase.write_db(data)
    SynDataBase.read_db(data)
    print(" other process running  ")
    all_processes = []
    for k in range(0, 50):
        pro = Process(target=SynDataBase.read_db, args=(data, ))
        all_processes.append(pro)
    for k in range(0, 10):
        pro = Process(target=SynDataBase.write_db, args=(data, ))
        all_processes.append(pro)
    for k in all_processes:
        k.start()
    for k in all_processes:
        k.join()


if __name__ == "__main__":
    main()