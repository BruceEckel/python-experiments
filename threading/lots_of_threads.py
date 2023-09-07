# lots_of_threads.py
import threading
from threading import Thread
import time


if __name__ == "__main__":
    threads = [Thread(target=lambda: time.sleep(10)) for _ in range(99)]
    for t in threads:
        t.start()
    print(f"{threading.enumerate() = }")
    print(f"{threading.main_thread() = }")
    print(f"{threading.main_thread().native_id = }")
    print(f"{threading.main_thread().is_alive() = }")
    print(f"{threading.active_count() = }")
    for t in threads:
        t.join()
