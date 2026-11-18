
# Incident Response Playbook 01: Brute-Force Attack

## 1. Objective
Provide steps to investigate and respond to suspected brute-force attacks.

## 2. Detection
- Windows Event ID: 4625
- Alert: Five or more failed logins within five minutes from one IP.

## 3. Triage
1. Identify the source IP address.
2. Identify the targeted account.
3. Review failed and successful login events.
4. Check whether other accounts are affected.

## 4. Containment
1. Block the suspicious IP if confirmed malicious and authorized.
2. Temporarily disable or protect the affected account if necessary.
3. Apply account lockout and MFA policies.

## 5. Eradication
1. Reset compromised passwords.
2. Remove unauthorized access.
3. Investigate other affected systems.

## 6. Recovery
1. Restore normal account access securely.
2. Monitor authentication activity.
3. Confirm that suspicious attempts have stopped.

## 7. Lessons Learned
Review detection thresholds and improve authentication monitoring.
