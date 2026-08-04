ip_counts = {}

with open("sample.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[parts.index("from") + 1]

            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

print("All failed login attempts by IP:")
print(ip_counts)

print("\nSuspicious IPs (3 or more failed attempts):")
for ip, count in ip_counts.items():
    if count >= 3:
        print(f"{ip} - {count} failed attempts")