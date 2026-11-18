
# Incident Case Report 01: Suspected Brute-Force Attack

**Project:** Detection Engineering & Threat Hunting Engagement  
**Analyst:** Swami Pravin Deshmukh  
**Date:** 18 November 2026

## 1. Incident Summary
A simulated brute-force login attempt was detected from source IP 192.168.1.100.

## 2. Detection Details
- Event ID: 4625
- Source IP: 192.168.1.100
- Failed attempts: 5
- Detection window: 5 minutes
- Severity: High

## 3. Investigation
The Python detection simulation grouped failed login events by source IP and checked the configured five-minute threshold.

Five failed attempts from the same IP generated an alert.

## 4. Impact Assessment
No real system compromise was established. The incident was simulated for detection testing.

## 5. Response Actions
- Identify the affected account.
- Review authentication logs.
- Check for successful logins from the same IP.
- Escalate suspicious activity for investigation.
- Apply account protection measures if required.

## 6. Conclusion
The brute-force detection simulation generated the expected alert.

## 7. Evidence
Python test output from test_brute_force.py.
