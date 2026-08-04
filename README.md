# \# SSH Log Analyser

# A Python command-line tool that parses SSH authentication logs to detect suspicious login activity, including brute-force attempts and potential account compromises.

# \## What it does

# \- Parses SSH log files line by line

# \- Counts failed login attempts per IP address

# \- Flags IPs with 3 or more failed attempts as suspicious (possible brute-force)

# \- Detects the highest-risk pattern: an IP that failed multiple times, then succeeded (possible account compromise)

# \- Tracks which usernames were most frequently targeted by attackers

# \## Why this matters

# Brute-force login attempts are one of the most common attack patterns against internet-facing servers. Security teams monitor for exactly this kind of pattern to detect and respond to potential breaches. This tool demonstrates the core logic behind that detection process.

# \## How to run it

# python log\_analyser.py <path\_to\_logfile>

# Example:

# python log\_analyser.py sample.log

# \## Example output

# Analysing log file: sample.log

# Suspicious IPs (3 or more failed attempts):

# 192.168.1.50 - 3 failed attempts

# 45.33.32.10 - 3 failed attempts

# 78.24.55.10 - 3 failed attempts

# HIGH ALERT - IP failed then succeeded (possible breach):

# 78.24.55.10 - failed 3 times, then logged in successfully!

# Most targeted usernames:

# admin - tried 2 times

# root - tried 1 times

# test - tried 3 times

# backup - tried 3 times

# \## Sample data

# sample.log contains fabricated SSH log entries for testing purposes, formatted to match real Linux auth.log output.

# \## Built with

# Python 3 (standard library only, no external dependencies)

# \## MITRE ATT\&CK Mapping

# This tool's detections align with the following MITRE ATT\&CK techniques:

# \- T1110 - Brute Force (Credential Access): Detecting IP addresses with repeated failed login attempts matches this technique, where attackers systematically guess credentials.

# \- T1078 - Valid Accounts (Defense Evasion, Persistence, Privilege Escalation, Initial Access): The failed-then-succeeded login pattern may indicate an attacker has obtained valid credentials, potentially through brute-forcing, and is now using them to gain legitimate-looking access.

# Reference: https://attack.mitre.org/

# \## Future improvements

# \- Export results to a CSV report

# \- Add a configurable threshold for suspicious activity (currently fixed at 3)

# \- Support real-time log monitoring instead of static file analysis

