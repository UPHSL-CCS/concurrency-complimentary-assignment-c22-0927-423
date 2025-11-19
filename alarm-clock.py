import threading
import time

# Shared flag to stop the stopwatch
stop_stopwatch = False

def stopwatch():
    seconds = 0
    while not stop_stopwatch:   # run while NOT stopped
        time.sleep(1)
        seconds += 1
        print(f"(⏱️) Stopwatch: {seconds} seconds")
    print("(⏱️) Stopwatch stopped. (｡•́︿•̀｡)")

def alarm_clock(alarm_after):
    global stop_stopwatch
    print(f"(⏰) Alarm set! Will ring after {alarm_after} seconds... (｡•̀ᴗ-)✧")
    time.sleep(alarm_after)
    print("\n🔔🔔🔔 ALARM RINGING!!! Wake uppp!! (˶˃ ᵕ ˂˶) .ᐟ.ᐟ 🔔🔔🔔\n")
    
    # Stop the stopwatch
    stop_stopwatch = True


print("૮ ˶ᵔ ᵕ ᵔ˶ ა\nConcurrency Demo: Alarm Clock + Stopwatch")
print("The stopwatch runs while the alarm waits in the background. ૮ ˶ᵔ ᵕ ᵔ˶ ა\n┊ ✩  ┊   ✧   ┊   ┊\n┊    ┊★      ┊   ✩⋆\n┊    ┊       ⊹˚ ⁭      ⁭ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭ ⁭\n✩⋆    ✮ \n")

# User input
alarm_input = int(input("Enter alarm time in seconds: "))

# Create threads
stopwatch_thread = threading.Thread(target=stopwatch)
alarm_thread = threading.Thread(target=alarm_clock, args=(alarm_input,))

# Start threads
stopwatch_thread.start()
alarm_thread.start()

# Wait for alarm to finish
alarm_thread.join()
stopwatch_thread.join()

print("\nProgram finished! (๑˃ᴗ˂)ﻭ✨")
