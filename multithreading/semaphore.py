""" Connecting cell phones to a charger """

# a semaphore is a data structure that allows a specific number of threads to lock "onto it"
# semaphores are used to track the availability of a limited resource
# several threads can lock and unlock the same lock

import random
import threading
import time

charger = threading.Semaphore(4)

def cellphone():
    name = threading.current_thread().getName()
    with charger: # context manager has an inbuild lock.acquire and lock.release
        print(name, 'is charging...')
        time.sleep(random.uniform(1,2))
        print(name, 'is DONE charging!')

if __name__ == '__main__':
    for phone in range(10):
        threading.Thread(target=cellphone, name='Phone-'+str(phone)).start()
