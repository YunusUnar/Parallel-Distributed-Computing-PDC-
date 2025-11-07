import threading
import time
from do_something import do_something

def task_runner(index, workload, result_store, gatekeeper):
    print(f"Task {index} requesting access...")
    with gatekeeper:
        print(f"Task {index} executing...")
        do_something(workload, result_store)
        print(f"Task {index} completed.")

def main():
    result_store = []
    gatekeeper = threading.Semaphore(2)  # max 2 threads allowed simultaneously
    total_tasks = 3
    workload = 7

    thread_group = [
        threading.Thread(target=task_runner, args=(n, workload, result_store, gatekeeper))
        for n in range(total_tasks)
    ]

    for thread in thread_group:
        thread.start()
    for thread in thread_group:
        thread.join()

    print("\nAggregated Results:", result_store)
    print("Total Entries (Semaphore):", len(result_store))

if __name__ == "__main__":
    main()
