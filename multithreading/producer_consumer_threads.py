""" Producers serving soup for Consumers to eat """

import queue
import threading
import time

serving_line = queue.Queue(maxsize=5) # python's queue module is designed for communication between threads
# it automatically handles all of the necessary locks and synchronisation mechanisms

def soup_producer():
    for i in range(20): # serve 20 bowls of soup
        serving_line.put_nowait('Bowl #'+str(i)) # put_nowait method will insert without blocking if the queue is full
        print('Served Bowl #', str(i), '- remaining capacity:', \
            serving_line.maxsize-serving_line.qsize())
        time.sleep(0.2) # time to serve a bowl of soup
    serving_line.put_nowait('no soup for you!') # twice, since there are two consumers
    serving_line.put_nowait('no soup for you!')

def soup_consumer():
    while True:
        bowl = serving_line.get()
        if bowl == 'no soup for you!':
            break
        print('Ate', bowl)
        time.sleep(0.3) # time to eat a bowl of soup

if __name__ == '__main__':
    for consumer in range(2): # with only once consumer, the queue would run full and the Queue module would raise a Full error
        threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()
