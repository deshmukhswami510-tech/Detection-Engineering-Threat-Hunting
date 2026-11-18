
# IOC Research Notes

**Project:** Detection Engineering & Threat Hunting Engagement  
**Analyst:** Swami Pravin Deshmukh  
**Date:** 18 November 2026

## 1. Objective
Document common Indicators of Compromise (IOCs) relevant to Windows security monitoring.

## 2. IP Address Indicators
- 192.0.2.10
- 198.51.100.7
- 203.0.113.15

These are documentation-only example IP addresses from reserved ranges, not confirmed malicious infrastructure.

## 3. File Indicators
- Unexpected executable files in temporary directories.
- Unknown DLL files loaded by suspicious processes.
- Unrecognized scripts in startup locations.

## 4. Process Indicators
- Encoded PowerShell execution.
- Unexpected rundll32.exe activity.
- Suspicious PsExec execution.
- Unusual scheduled task creation.

## 5. Account Indicators
- Repeated failed login attempts.
- Unexpected account creation.
- Account lockout events.
- Unusual remote desktop logins.

## 6. Investigation Sources
- Windows Security Event Logs
- Windows Defender alerts
- MITRE ATT&CK knowledge base
- VirusTotal for future hash and file research

## 7. Conclusion
These indicators provide starting points for threat hunting. Each indicator must be investigated and validated before being classified as malicious.
