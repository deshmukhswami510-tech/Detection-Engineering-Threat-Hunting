
from datetime import datetime, timedelta

events = []

start_time = datetime(2026, 11, 18, 10, 0, 0)

# IP 1: Five failed attempts spread over 8 minutes
for i in range(5):
    events.append({
        "EventID": 4625,
        "SourceIP": "192.168.1.100",
        "Time": start_time + timedelta(minutes=i * 2)
    })

# IP 2: Only three failed attempts
for i in range(3):
    events.append({
        "EventID": 4625,
        "SourceIP": "192.168.1.200",
        "Time": start_time + timedelta(minutes=i)
    })

# IP 3: Successful login (should not trigger an alert)
events.append({
    "EventID": 4624,
    "SourceIP": "192.168.1.300",
    "Time": start_time
})

print("=== BRUTE FORCE DETECTION TEST ===")

failed_logins = {}

for event in events:
    if event["EventID"] == 4625:
        ip = event["SourceIP"]
        failed_logins.setdefault(ip, []).append(event["Time"])

alert_found = False

for ip, timestamps in failed_logins.items():
    timestamps.sort()

    for i in range(len(timestamps)):
        window_end = timestamps[i] + timedelta(minutes=5)

        count = sum(
            1 for timestamp in timestamps
            if timestamps[i] <= timestamp <= window_end
        )

        if count >= 5:
            print("[ALERT] Possible brute-force attack detected!")
            print("Source IP:", ip)
            print("Failed attempts:", count)
            alert_found = True
            break

if not alert_found:
    print("[INFO] No brute-force activity detected.")
