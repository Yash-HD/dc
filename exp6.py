import csv

processes = ["P1", "P2", "P3"]

# Initialize vector clocks
clock = {}

for p in processes:
    clock[p] = [0, 0, 0]

messages = {}
events = []

filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        p = row["process_id"]
        action = row["event_action"].upper()
        target = row["target_process"]

        index = processes.index(p)

        if action == "SEND":

            clock[p][index] += 1

            messages[(p, target)] = clock[p].copy()

        elif action == "RECEIVE":

            msg = messages[(target, p)]

            for i in range(3):
                clock[p][i] = max(clock[p][i], msg[i])

            clock[p][index] += 1

        else:
            clock[p][index] += 1

        events.append((row["event_id"], clock[p].copy()))

        print(row["event_id"], p, ":", clock[p])


# Compare vector clocks
print("\nCausal Relationships:")

for i in range(len(events)):
    for j in range(i + 1, len(events)):

        e1, v1 = events[i]
        e2, v2 = events[j]

        if all(v1[k] <= v2[k] for k in range(3)) and v1 != v2:
            print(e1, "causally precedes", e2)

        elif all(v2[k] <= v1[k] for k in range(3)) and v1 != v2:
            print(e2, "causally precedes", e1)

        else:
            print(e1, "and", e2, "are concurrent")