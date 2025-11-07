import multiprocessing
import time
from do_something import do_something

def task_handler():
    proc_name = multiprocessing.current_process().name
    print(f"[🟢] Initiating {proc_name}\n")

    if proc_name == 'daemon_task':
        for count in range(5):
            print(f"--> Step {count}\n")
        time.sleep(1)
    else:
        output_data = []
        do_something(3, output_data)
        print(f"[📊] Computation results: {output_data}")
        time.sleep(1)

    print(f"[🔚] Terminating {proc_name}\n")

if __name__ == '__main__':
    daemon_task = multiprocessing.Process(
        name='daemon_task', target=task_handler)
    daemon_task.daemon = False

    regular_task = multiprocessing.Process(
        name='regular_task', target=task_handler)
    regular_task.daemon = False

    daemon_task.start()
    regular_task.start()
