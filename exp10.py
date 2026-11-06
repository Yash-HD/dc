import csv
import threading

A = []
B = [
    [1, 2, 3, 4],
    [2, 1, 2, 1],
    [3, 2, 1, 2],
    [1, 3, 2, 1]
]

result = []

# Worker function
def multiply(row, index):

    print("Worker", index, "calculating row")

    new_row = []

    for j in range(4):

        total = 0

        for k in range(4):
            total += row[k] * B[k][j]

        new_row.append(total)

    result[index] = new_row


# Read matrix A from CSV
filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        A.append([
            int(row["col_0"]),
            int(row["col_1"]),
            int(row["col_2"]),
            int(row["col_3"])
        ])

# Initialize result matrix
result = [None] * len(A)

threads = []

print("\nMaster scattering rows to workers")

# Create one worker for each row
for i in range(len(A)):

    t = threading.Thread(
        target=multiply,
        args=(A[i], i)
    )

    threads.append(t)
    t.start()

# Wait for workers
for t in threads:
    t.join()

# Gather results
print("\nMaster gathering results")

print("Final Matrix:")

for row in result:
    print(row)