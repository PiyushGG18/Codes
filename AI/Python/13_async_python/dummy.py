# import threading
# import time

# def brew(name):
#     print(f"Brewing {name}...")
#     time.sleep(3)
#     print(f"{name} is ready...")

# threads = [
#     threading.Thread(target=brew, args=("Masala chai",)),
#     threading.Thread(target=brew, args=("Green chai",)),
#     threading.Thread(target=brew, args=("Ginger chai",)),
#     ]

# [t.start() for t in threads]
# [t.join() for t in threads]

from multiprocessing import Process
import time

def brew(name):
    print(f"Brewing {name}...")
    time.sleep(3)
    print(f"{name} is ready...")

if __name__ == "__main__":
    processes = [
        Process(target=brew, args=("Masala chai",)),
        Process(target=brew, args=("Green chai",)),
        Process(target=brew, args=("Ginger chai",)),
        ]

    [t.start() for t in processes]
    [t.join() for t in processes]