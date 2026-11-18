
# Incident Response Playbook 02: Suspicious PowerShell Activity

## 1. Objective
Investigate potentially malicious PowerShell execution.

## 2. Detection
- Windows Event ID: 4688
- Suspicious arguments: -enc or -encodedcommand

## 3. Triage
1. Identify the affected endpoint.
2. Review the PowerShell command line.
3. Identify the executing user.
4. Check parent process and execution time.

## 4. Containment
1. Isolate the endpoint if malicious activity is confirmed and authorized.
2. Stop suspicious processes when appropriate.
3. Restrict the compromised account if necessary.

## 5. Eradication
1. Remove malicious scripts and files.
2. Investigate persistence mechanisms.
3. Scan the endpoint for additional threats.

## 6. Recovery
1. Restore the endpoint after verification.
2. Reset compromised credentials if needed.
3. Monitor PowerShell activity.

## 7. Lessons Learned
Improve PowerShell logging and detection coverage.
