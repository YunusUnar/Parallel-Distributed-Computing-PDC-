from do_something import *
import time
import multiprocessing
import threading

def run_parallel(target_func, count, use_threads=False):
    jobs = []
    out_list = multiprocessing.Manager().list() if not use_threads else []

    for _ in range(count):
        if use_threads:
            job = threading.Thread(target=target_func, args=(size, out_list))
        else:
            job = multiprocessing.Process(target=target_func, args=(size, out_list))
        jobs.append(job)

    start_time = time.time()

    for job in jobs:
        job.start()
    for job in jobs:
        job.join()

    end_time = time.time()
    mode = "Multithreading" if use_threads else "Multiprocessing"
    print(f"{mode} complete.")
    print(f"{mode} time = {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    size = 1000
    procs = 50
    threads = 50

    run_parallel(do_something, procs, use_threads=False)
    run_parallel(do_something, threads, use_threads=True)
