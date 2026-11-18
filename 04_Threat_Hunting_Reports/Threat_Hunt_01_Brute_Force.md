
# Threat Hunting Report 01: Brute-Force Attack

**Project:** Detection Engineering & Threat Hunting Engagement  
**Analyst:** Swami Pravin Deshmukh  
**Date:** 18 November 2026

## 1. Objective
Identify repeated failed Windows login attempts that may indicate a brute-force attack.

## 2. Data Source
- Windows Security Event Logs
- Event ID: 4625 (Failed Logon)

## 3. Hunting Hypothesis
An attacker may attempt multiple passwords against a Windows account from the same source IP address.

## 4. Hunting Method
- Group failed login events by source IP.
- Check the number of failed attempts.
- Examine whether five or more attempts occur within five minutes.
- Compare activity from different source IP addresses.

## 5. Findings
A Python simulation was used to test the detection logic.

- IP 192.168.1.100: Five failed attempts within five minutes generated an alert.
- IP 192.168.1.200: Three failed attempts did not generate an alert.
- Five attempts spread over eight minutes did not generate an alert.
- Successful login events (Event ID 4624) were excluded.

## 6. Conclusion
The simulation successfully identified the configured brute-force threshold and time window. This test used simulated events, not live Windows security logs.

## 7. Recommendation
Monitor repeated failed logins, investigate suspicious source IP addresses, and review affected accounts.
