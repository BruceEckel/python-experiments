# lots_of_threads.py
import threading
from threading import Thread
import time


if __name__ == "__main__":
    threads = [
        Thread(target=lambda: time.sleep(10))
        for _ in range(99)
    ]
    for t in threads:
        t.start()
    print(
        f"""
    {threading.enumerate() = }
    {threading.main_thread() = }
    {threading.main_thread().native_id = }
    {threading.main_thread().is_alive() = }
    {threading.active_count() = }
    """
    )
    for t in threads:
        t.join()
