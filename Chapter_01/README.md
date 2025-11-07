---

 🧪 Python Performance Test: Threads vs Processes

This experiment explores how Python handles parallel execution using two distinct approaches — **multithreading** and **multiprocessing**. The goal is to evaluate their efficiency when executing a repetitive task involving mathematical operations and simulated delays.

---

 ⚙️ Setup Overview

- **Programming Language**: Python 3  
- **Modules Used**: `threading`, `multiprocessing`, `time`  
- **Task Complexity**: 1000 iterations per unit  
- **Platform**: Windows 10  

The core function performs repeated calculations (square roots and exponentiation) and stores results in a shared list. The same function is executed using both threads and processes to compare performance.

---

 🔄 Test Scenarios

We ran the function under three different concurrency levels:

| Configuration | Process Execution Time | Thread Execution Time |
|---------------|------------------------|------------------------|
| 5 Units       | 1.428 seconds          | 0.044 seconds          |
| 10 Units      | 2.438 seconds          | 0.041 seconds          |
| 50 Units      | 8.716 seconds          | 0.099 seconds          |

---

 📊 Key Observations

- **Threads were consistently faster** across all test cases.
- The task was **I/O-bound**, meaning it involved waiting (e.g., `time.sleep`), not heavy computation.
- Python’s **Global Interpreter Lock (GIL)** didn’t hinder thread performance due to the nature of the task.

---

 🧵 Why Threads Excelled

- Threads share memory space and switch context quickly.
- While one thread waits, others continue working.
- Minimal overhead compared to spawning full processes.

---

 🔀 Why Processes Lagged

- Each process runs in its own memory space.
- Communication between processes adds latency.
- For small workloads, the overhead of managing processes outweighs the benefits.

---

🧠 Final Takeaway

- For **I/O-heavy operations** (like file access, network calls, or sleep delays), **multithreading** is the better choice.
- For **CPU-intensive tasks** (like image rendering or large-scale data crunching), **multiprocessing** is more suitable as it leverages multiple cores and avoids GIL limitations.

In this specific test, multithreading was clearly more efficient.

---

 ▶️ How to Execute

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   ```

2. **Run the script**  
   ```bash
   python Process_thread.py
   ```

---
