import multiprocessing
import time
from do_something import do_something

def execute_job():
    shared_results = multiprocessing.Manager().list()
    print("[🟢] Job initiated")
    do_something(10, shared_results)
    print(f"[✅] Job completed with {len(shared_results)} entries")

def observe_process(p):
    print("[👀] Initial state:", p, p.is_alive())
    p.start()
    print("[🏃] In progress:", p, p.is_alive())
    time.sleep(2)
    p.terminate()
    print("[⛔] Force stopped:", p, p.is_alive())
    p.join()
    print("[🔚] Cleanup done:", p, p.is_alive())
    print("[📤] Final exit code:", p.exitcode)

if __name__ == "__main__":
    worker = multiprocessing.Process(target=execute_job)
    observe_process(worker)
