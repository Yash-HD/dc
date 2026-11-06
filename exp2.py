import csv

alive = []
filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["is_alive"].upper() == "TRUE":
            alive.append(int(row["node_id"]))

# Find initiator (lowest active node ID)
initiator = min(alive)

print("Coordinator failed!")
print("Node", initiator, "starts election")

# Send election messages to higher active nodes
for node in alive:
    if node > initiator:
        print("ELECTION sent to Node", node)
        print("OK received from Node", node)

# Highest active node becomes coordinator
leader = max(alive)

print("\nNode", leader, "broadcasts COORDINATOR")
print("New Coordinator is Node", leader)