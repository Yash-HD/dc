import csv

workers = ["Worker_1", "Worker_2", "Worker_3"]

load = {}

for w in workers:
    load[w] = 0

filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    jobs = list(reader)

# Round Robin allocation
for i, job in enumerate(jobs):

    worker = workers[i % len(workers)]

    job["assigned_worker"] = worker
    job["status"] = "COMPLETED"

    load[worker] += int(job["compute_units"])

    print(job["job_id"], "assigned to", worker)

# Display worker loads
print("\nWorker Load Summary:")

for w in workers:
    print(w, ":", load[w], "compute units")

print("\nAll jobs allocated successfully!")