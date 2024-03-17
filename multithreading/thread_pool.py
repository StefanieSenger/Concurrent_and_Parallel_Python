""" Chopping vegetables with a ThreadPool """

import threading
from concurrent.futures import ThreadPoolExecutor

def vegetable_chopper(vegetable_id):
    name = threading.current_thread().getName()
    print(name, 'chopped vegetable', vegetable_id)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5) # we are re-using five threads to execute all 100 tasks
    for vegetable in range(100):
        # we only need to add functions to the pool; it creates threads from it under the hood
        pool.submit(vegetable_chopper, vegetable)
    # free up any resource the pool is using:
    pool.shutdown() # by default wait=True, so all threads finish before shutting down
