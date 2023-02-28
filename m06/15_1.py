import multiprocessing 
from datetime import datetime
import time
import random


def print_time():
    now = datetime.now()
    print("Today's date and time is {}".format(now))
    time.sleep(random.random())


if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=print_time())
    process_2 = multiprocessing.Process(target=print_time())
    process_3 = multiprocessing.Process(target=print_time())
    process_1.start()
    process_2.start()
    process_3.start()
    process_1.join()
    process_2.join()
    process_3.join()