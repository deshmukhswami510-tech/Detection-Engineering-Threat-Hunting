
# False Positive Tuning Report

**Project:** Detection Engineering & Threat Hunting Engagement  
**Analyst:** Swami Pravin Deshmukh

## 1. Brute-Force Detection

**Rule:** windows_brute_force_correlation.yml

**Potential False Positive:** Users repeatedly entering incorrect passwords.

**Tuning Approach:**
- Require five or more failed attempts within five minutes.
- Group events by source IP.
- Exclude successful login events.

**Expected Benefit:** Reduces alerts caused by a small number of incorrect password attempts.

## 2. Encoded PowerShell Detection

**Rule:** windows_powershell_encoded.yml

**Potential False Positive:** Authorized administrators using encoded PowerShell commands.

**Tuning Approach:**
- Review the executing user and parent process.
- Check whether the command is authorized.
- Exclude verified administrative activity only after testing.

**Expected Benefit:** Helps distinguish authorized administration from suspicious execution.

## 3. Scheduled Task Detection

**Rule:** windows_suspicious_scheduled_task.yml

**Potential False Positive:** Legitimate software creating scheduled tasks.

**Tuning Approach:**
- Review the task name and command.
- Check the task creator and execution path.
- Maintain an approved list of known administrative tasks.

**Expected Benefit:** Reduces unnecessary alerts from legitimate scheduled task creation.

## Conclusion

Three detection rules have documented false-positive scenarios and proposed tuning approaches. These approaches require validation against real event data before being considered fully tuned.
