import sys

if len(sys.argv) < 2:
    print("Usage: python log_analyser.py <logfile>")
    sys.exit(1)

log_file = sys.argv[1]

failed_ips = {}
success_ips = set()
targeted_usernames = {}

with open(log_file, "r") as file:
    for line in file:
        parts = line.split()

        if "Failed password" in line:
            ip = parts[parts.index("from") + 1]
            if ip in failed_ips:
                failed_ips[ip] += 1
            else:
                failed_ips[ip] = 1

            username = parts[parts.index("for") + 1]
            if username == "invalid":
                username = parts[parts.index("user") + 1]

            if username in targeted_usernames:
                targeted_usernames[username] += 1
            else:
                targeted_usernames[username] = 1

        elif "Accepted password" in line:
            ip = parts[parts.index("from") + 1]
            success_ips.add(ip)

print(f"Analysing log file: {log_file}\n")

print("All failed login attempts by IP:")
print(failed_ips)

print("\nSuspicious IPs (3 or more failed attempts):")
for ip, count in failed_ips.items():
    if count >= 3:
        print(f"{ip} - {count} failed attempts")

print("\nHIGH ALERT - IP failed then succeeded (possible breach):")
for ip in failed_ips:
    if ip in success_ips:
        print(f"{ip} - failed {failed_ips[ip]} times, then logged in successfully!")

print("\nMost targeted usernames:")
for username, count in targeted_usernames.items():
    print(f"{username} - tried {count} times")