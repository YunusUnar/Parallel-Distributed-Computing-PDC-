import multiprocessing
from do_something import do_something

def execute_job(task_id):
    print(f"[🔧] Worker {task_id} initiated")
    results = multiprocessing.Manager().list()
    do_something(task_id * 1000, results)
    print(f"[✅] Worker {task_id} completed with {len(results)} items")

def start_workers():
    for task in range(6):
        worker = multiprocessing.Process(target=execute_job, args=(task,))
        worker.start()
        worker.join()

if __name__ == "__main__":
    start_workers()
