failed_ips = {}
success_ips = set()

with open("sample.log", "r") as file:
    for line in file:
        parts = line.split()

        if "Failed password" in line:
            ip = parts[parts.index("from") + 1]
            if ip in failed_ips:
                failed_ips[ip] += 1
            else:
                failed_ips[ip] = 1

        elif "Accepted password" in line:
            ip = parts[parts.index("from") + 1]
            success_ips.add(ip)

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