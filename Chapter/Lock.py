import threading
import time
from do_something import do_something

def execute_task(id, workload, results, sync_lock):
    print(f"Executing thread {id}...")
    with sync_lock:
        do_something(workload, results)
    print(f"Thread {id} completed.")

def main():
    results = []
    sync_lock = threading.Lock()

    total_threads = 3
    workload_size = 7

    thread_pool = [
        threading.Thread(target=execute_task, args=(idx, workload_size, results, sync_lock))
        for idx in range(total_threads)
    ]

    for thread in thread_pool:
        thread.start()
        time.sleep(0.5)  # intentional delay to visualize execution order

    for thread in thread_pool:
        thread.join()

    print("\nCollected Results:", results)
    print("Total Items (with Lock):", len(results))

if __name__ == "__main__":
    main()
