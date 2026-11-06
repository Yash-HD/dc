import csv

def processData(x):
    return int(x) * 2

filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        print("\n[DISPATCH]")
        print(row["client_name"], "invoking", row["method_name"])

        # Marshalling
        request = (row["method_name"], row["param_value"])

        # Server execution
        method, parameter = request

        print("[SERVER EXECUTION]")
        print("Processing parameter:", parameter)

        result = processData(parameter)

        print("[RETURN]")
        print("Result:", result)