import csv

clock = {}
messages = {}

filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        p = row["process_id"]
        event = row["event_type"].upper()
        target = row["message_to"]

        if p not in clock:
            clock[p] = int(row["initial_clock"])

        if event == "RECEIVE":
            clock[p] = max(clock[p], messages[(target, p)]) + 1

        else:
            clock[p] += 1

        if event == "SEND":
            messages[(p, target)] = clock[p]

        print(row["event_id"], "Clock:", clock[p])