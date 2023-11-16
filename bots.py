import threading
import time
import json

with open('inventory.dat', 'r') as file:
   inventory = json.load(file)

def bot_clerk(items):
    cart = []
    lock = threading.Lock()
    fetcher_lists = [[], [], []]
    for i, item in enumerate(items):
        fetcher_lists[i % 3].append(item)
    threads = []
    for list in fetcher_lists:
        thread = threading.Thread(target=bot_fetcher, args=(list, cart, lock))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    return cart


def bot_fetcher(items, cart, lock):
    for item in items:
        time.sleep(inventory[item][1])
        with lock:
            cart.append([item, inventory[item][0]])


