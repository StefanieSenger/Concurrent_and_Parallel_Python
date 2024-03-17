""" Two shoppers adding garlic and potatoes to a shared notepad """

import threading

garlic_count = 0
potato_count = 0
pencil = threading.RLock() # <-- reentrant lock, instead of normal lock,
# because otherwise would block because of recursive locking
# RLock()s must be released by the same thread than the one that acquired it (other than a usual Lock())
# RLock()s must be released the same number of times it was acquired

def add_garlic():
    global garlic_count
    pencil.acquire()
    garlic_count += 1
    pencil.release()

def add_potato():
    global potato_count
    pencil.acquire()
    potato_count += 1
    add_garlic()
    pencil.release()

def shopper():
    for i in range(10_000):
        add_garlic()
        add_potato()

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('We should buy', garlic_count, 'garlic.')
    print('We should buy', potato_count, 'potatoes.')
