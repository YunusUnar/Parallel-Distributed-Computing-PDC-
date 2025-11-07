import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
from do_something import do_something

def synchronized_worker(barrier, mutex):
    proc_name = multiprocessing.current_process().name
    barrier.wait()
    current_time = datetime.fromtimestamp(time())
    with mutex:
        print(f"{proc_name} >>> {current_time}")
        results = []
        do_something(2, results)
        print(f"{proc_name} output: {results}")

def independent_worker():
    proc_name = multiprocessing.current_process().name
    current_time = datetime.fromtimestamp(time())
    print(f"{proc_name} >>> {current_time}")
    results = []
    do_something(2, results)
    print(f"{proc_name} output: {results}")

def initiate_jobs():
    barrier = Barrier(2)
    mutex = Lock()

    job_list = [
        Process(name="worker-A (barrier)", target=synchronized_worker, args=(barrier, mutex)),
        Process(name="worker-B (barrier)", target=synchronized_worker, args=(barrier, mutex)),
        Process(name="worker-C (no barrier)", target=independent_worker),
        Process(name="worker-D (no barrier)", target=independent_worker),
    ]

    for job in job_list:
        job.start()

if __name__ == "__main__":
    initiate_jobs()
