import csv
import threading
import time

completed = []
lock = threading.Lock()

# Function executed by each thread
def process_task(task):

    print(task["thread_name"], "processing", task["task_id"])

    # Simulate task processing
    time.sleep(int(task["burst_ms"]) / 1000)

    # Critical section
    lock.acquire()

    print(task["thread_name"], "acquired lock")

    task["status"] = "COMPLETED"
    completed.append(task["task_id"])

    print(task["thread_name"], "released lock")

    lock.release()


# Read CSV
filename = input("Enter CSV filename: ")

threads = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        t = threading.Thread(
            target=process_task,
            args=(row,)
        )

        threads.append(t)
        t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("\nCompleted Tasks:", completed)