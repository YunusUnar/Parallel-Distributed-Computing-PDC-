---

🔐 Python Thread Control Techniques  
**(Using Lock, RLock, Semaphore, and Condition)**

This demonstration explores how various synchronization tools from Python’s `threading` module manage concurrent access to a shared resource. The computational logic is based on a common function defined in `do_something.py`, which performs repeated operations and appends results to a shared list.

---

### 🧵 Synchronization Strategies Explored

#### 1. Basic Lock  
- **Intent**: Prevents multiple threads from modifying shared data simultaneously.  
- **Execution Pattern**:  
  ```
  Thread 0 active... done.  
  Thread 1 active... done.  
  Thread 2 active... done.  
  ```
- **Outcome**: Shared list updated safely; final count = 21.

#### 2. Reentrant Lock (RLock)  
- **Intent**: Allows a thread to acquire the same lock multiple times without deadlock.  
- **Execution Pattern**: Mirrors basic Lock behavior with consistent thread sequencing.  
- **Outcome**: Reliable and safe updates; final count = 21.

#### 3. Semaphore  
- **Intent**: Restricts the number of threads accessing a resource concurrently.  
- **Execution Pattern**:  
  ```
  Thread 0 waiting... started.  
  Thread 1 waiting... started.  
  Thread 2 waiting... started.  
  ```
  Threads proceed in controlled batches.  
- **Outcome**: List integrity preserved; final count = 21.

#### 4. Condition Variable  
- **Intent**: Enables threads to pause until a specific condition is met, then resume.  
- **Execution Pattern**:  
  ```
  Thread 0 signals condition.  
  Thread 1 signals condition.  
  Thread 2 signals condition.  
  Monitor: List size = 7 → 14 → 21  
  ```
- **Outcome**: Threads coordinate effectively; progress tracked accurately.

---

### 📋 Comparison Summary

| Mechanism   | Purpose                          | Behavior Style         | Safety Level | Ideal Use Case               |
|-------------|----------------------------------|-------------------------|--------------|------------------------------|
| Lock        | Exclusive access enforcement     | Sequential execution    | ✅ Safe       | General thread protection    |
| RLock       | Nested locking support           | Similar to Lock         | ✅ Safe       | Recursive lock scenarios     |
| Semaphore   | Limit concurrent thread access   | Batched execution       | ✅ Safe       | Resource pool management     |
| Condition   | Wait/notify coordination         | Event-driven signaling  | ✅ Safe       | Producer-consumer workflows  |

---

### 🧠 Final Thoughts

Each synchronization method tested — Lock, RLock, Semaphore, and Condition — effectively preserved data consistency during parallel execution. All approaches yielded the expected result: a shared list with 21 entries and no race conditions.

- **Lock/RLock**: Best for simple mutual exclusion.
- **Semaphore**: Ideal when limiting simultaneous access to finite resources.
- **Condition**: Useful for complex coordination between threads based on state or signals.

Choose the synchronization primitive that aligns with your concurrency model and resource constraints.

---

### ▶️ Execution Instructions

Run each script individually to observe its behavior:

```bash
python Chapter_02/Lock.py
python Chapter_02/RLock.py
python Chapter_02/Semaphore.py
python Chapter_02/Condition.py
```

---
