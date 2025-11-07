

##  Exploring Python Multiprocessing: Hands-On Examples

This section dives into Python’s `multiprocessing` capabilities by walking through practical scenarios that demonstrate how to launch, label, coordinate, monitor, and gracefully shut down multiple processes. All examples revolve around a shared CPU-intensive function from `do_something.py`.

---

###  1. custom_naming.py  
**Objective**: Assign identifiable names to processes and measure execution time.  
**Example**:
```python
multiprocessing.Process(name='worker_one', target=do_something, args=(1000, out_list1))
multiprocessing.Process(target=do_something, args=(1000, out_list2))
```
**Result**:
```
worker_one output size: 1000  
Unnamed process output size: 1000  
Elapsed time: 0.43 seconds
```
**Takeaway**: Named and unnamed processes executed in parallel, improving performance over sequential execution.

---

###  2. dynamic_spawning.py  
**Objective**: Generate multiple processes programmatically in a loop.  
**Example**:
```python
for i in range(6):
    multiprocessing.Process(target=myFunc, args=(i,)).start()
```
**Result**:  
Each spawned process handled a workload of `i * 1000` independently.  
**Takeaway**: Demonstrated scalable parallelism with predictable output per worker.

---

###  3. process_lifecycle.py  
**Objective**: Showcase process control — starting, terminating, and joining.  
**Example**:
```python
p.start(); p.terminate(); p.join()
```
**Result**:
```
Process launched and terminated successfully  
Exit status: 0
```
**Takeaway**: Validated safe lifecycle handling using `.start()`, `.terminate()`, and `.join()`.

---

###  4. daemon_vs_regular.py  
**Objective**: Contrast daemon and non-daemon process behavior.  
**Example**:
```python
background_process.daemon = True  
regular_process.daemon = False
```
**Result**:
```
Daemon exited with main program  
Regular process completed and returned data
```
**Takeaway**: Daemons are tied to the main thread’s lifespan; regular processes run independently.

---

###  5. sync_with_barrier.py  
**Objective**: Coordinate process execution using `Barrier` and `Lock`.  
**Example**:
```python
Barrier(2), Lock()
```
**Result**:  
Processes paused at the barrier and printed results in synchronized order.  
**Takeaway**: Barrier ensured alignment; Lock protected shared data access.

---

###  6. pool_execution.py  
**Objective**: Use a process pool for efficient parallel computation.  
**Example**:
```python
pool.map(do_something, range(10))
```
**Result**:
```
Computed squares: [0, 1, 4, ..., 81]
```
**Takeaway**: Tasks were evenly distributed across 4 workers, maximizing CPU usage.

---

###  Summary Overview

| Script Name                  | Purpose                          | ✅ | Key Insight                                |
|-----------------------------|----------------------------------|----|---------------------------------------------|
| custom_naming.py            | Process labeling & timing        | ✅ | Easier debugging with named workers         |
| dynamic_spawning.py         | Loop-based process creation      | ✅ | Scalable and isolated execution             |
| process_lifecycle.py        | Start/stop/join demonstration    | ✅ | Controlled shutdown and cleanup             |
| daemon_vs_regular.py        | Daemon vs non-daemon comparison  | ✅ | Daemons exit early; regulars complete tasks |
| sync_with_barrier.py        | Coordination with Barrier & Lock | ✅ | Ordered and safe execution                  |
| pool_execution.py           | Parallelism using Pool           | ✅ | Efficient task distribution                 |

---

###  Key Learnings

- Multiprocessing enables true parallel execution for CPU-bound workloads.
- Naming processes improves traceability and debugging.
- Daemon threads are short-lived; regular ones persist until completion.
- Synchronization primitives like Barrier and Lock help manage concurrency safely.
- Pools simplify task distribution across multiple workers.

---

