
# Threat Hunting Report 02: Suspicious PowerShell Activity

**Project:** Detection Engineering & Threat Hunting Engagement  
**Analyst:** Swami Pravin Deshmukh  
**Date:** 18 November 2026

## 1. Objective
Identify suspicious PowerShell execution that may indicate malicious activity.

## 2. Data Source
- Windows Process Creation Logs
- Event ID: 4688
- Process command-line information

## 3. Hunting Hypothesis
Attackers may use encoded PowerShell commands to hide malicious instructions.

## 4. Hunting Method
- Review PowerShell process execution.
- Examine command-line arguments.
- Look for -enc and -encodedcommand.
- Identify unusual or unauthorized executions.

## 5. Findings
A Sigma detection rule was created to identify PowerShell commands containing encoded-command arguments.

The YAML file passed syntax validation. No live attack or real Windows event investigation was performed.

## 6. Conclusion
Encoded PowerShell execution is a useful activity to monitor because it can be abused to conceal commands.

## 7. Recommendation
Monitor encoded PowerShell commands and investigate their source, user account, and execution context.
