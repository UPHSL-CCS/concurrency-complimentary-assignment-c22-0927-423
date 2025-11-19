# 🕰️ Alarm Clock + Stopwatch Concurrency Demo

Submitted by: Cabanes, Angela -- J4A

This is a simple Python program that demonstrates **concurrency** using threads.  
The program simulates:

1. A **stopwatch** that continuously counts seconds. ⏱️  
2. An **alarm clock** that rings after a user-defined time. ⏰  

Both tasks run concurrently, showing how multiple things can happen at the same time in a program.

---

## 🌟 How It Works

- **Stopwatch thread**: Prints the elapsed time every second.  
- **Alarm thread**: Waits for the user-specified number of seconds, then rings and stops the stopwatch.  
- **Shared variable**: `stop_stopwatch` is used for communication between threads so the stopwatch knows when to stop.  
- **Main thread**: Keeps the program alive and waits for both threads to finish.

The stopwatch keeps running while the alarm is waiting, which shows that **one task does not block the other**.  

---

## 💡 Why This is Concurrency

This program is an example of **concurrency** because:

- Multiple tasks (stopwatch & alarm) are managed *at the same time* in the program.  
- They overlap in execution: the stopwatch continues ticking while the alarm sleeps in the background.  
- Even though Python may not run them on separate CPU cores (that would be **parallelism**), the program still handles multiple tasks simultaneously, which is the essence of concurrency.  
- Users can see the effect immediately: the stopwatch never freezes while waiting for the alarm.

---

## 📝 How to Run

1. Make sure you have Python installed. 🐍  
2. Save the script as `alarm_stopwatch.py`.  
3. Run the program:

```bash
python alarm_stopwatch.py
