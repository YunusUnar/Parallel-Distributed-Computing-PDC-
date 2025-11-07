import multiprocessing
from do_something import do_something

def process_element(value):
    buffer = []
    do_something(2, buffer)  # simulate CPU work
    return value ** 2

def execute_with_pool(data_list, workers):
    with multiprocessing.Pool(processes=workers) as executor:
        outcome = executor.map(process_element, data_list)
    return outcome

if __name__ == "__main__":
    DATA = list(range(10))
    WORKER_COUNT = 4

    results = execute_with_pool(DATA, WORKER_COUNT)
    print("Processed Output:", results)
