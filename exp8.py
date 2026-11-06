import csv

filename = input("Enter CSV filename: ")

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        t0 = float(row["t0_send_ms"])
        ts = float(row["t_server_ms"])
        t1 = float(row["t1_recv_ms"])

        # Calculate RTT
        rtt = t1 - t0

        # Estimate server time
        estimated = ts + (rtt / 2)

        # Calculate client clock adjustment
        offset = estimated - t1

        adjusted = t1 + offset

        print("\nClient:", row["client_id"])
        print("RTT:", rtt, "ms")
        print("Estimated Server Time:", estimated, "ms")
        print("Clock Offset:", offset, "ms")
        print("Adjusted Client Time:", adjusted, "ms")