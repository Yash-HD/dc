import csv

nodes = []

filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        nodes.append(row)

# Calculate average of non-faulty clocks
total = 0
count = 0

for node in nodes:
    if node["is_faulty"].upper() == "FALSE":
        total += float(node["clock_time_sec"])
        count += 1

average = total / count

print("Average Clock Time:", average)

# Calculate adjustment for each node
print("\nClock Adjustments:")

for node in nodes:
    if node["is_faulty"].upper() == "FALSE":

        current = float(node["clock_time_sec"])
        adjustment = average - current

        print(node["node_id"], "Adjustment:", adjustment, "seconds")

    else:
        print(node["node_id"], "is faulty. Ignored.")