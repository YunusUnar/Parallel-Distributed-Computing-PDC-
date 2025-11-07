import multiprocessing
import time
from do_something import do_something

def execute_parallel_jobs(task_size):
    results_a = multiprocessing.Manager().list()
    results_b = multiprocessing.Manager().list()

    job_a = multiprocessing.Process(
        name="Processor-A",
        target=do_something,
        args=(task_size, results_a)
    )

    job_b = multiprocessing.Process(
        target=do_something,
        args=(task_size, results_b)
    )

    start_time = time.time()
    job_a.start()
    job_b.start()

    job_a.join()
    job_b.join()
    end_time = time.time()

    return results_a, results_b, end_time - start_time

if __name__ == "__main__":
    TASK_LOAD = 1000
    output_a, output_b, elapsed = execute_parallel_jobs(TASK_LOAD)

    print(f"Processor-A result count: {len(output_a)}")
    print(f"Processor-B result count: {len(output_b)}")
    print(f"Total runtime: {elapsed:.2f} seconds")
