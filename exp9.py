import csv

active = []

filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["is_active"].upper() == "TRUE":
            active.append(int(row["node_id"]))

print("Coordinator failed!")
print("Election started")

current = min(active)
token =[]
# Circulate token around the ring
for node in active:
    print("Token passed to Node", node)
    token.append(node)

# Highest ID becomes leader
leader = max(token)

print("\nElection token:", token)
print("New Coordinator is Node", leader)
print("Node", leader, "broadcasts COORDINATOR")