import re

patterns = {
    "aws_access_key": {
        "regex": r"AKIA[0-9A-Z]{16}",
        "severity": "HIGH"
    },

    "credit_card": {
        "regex": r"\\b(?:\\d[ -]*?){13,16}\\b",
        "severity": "HIGH"
    },

    "jwt_token": {
        "regex": r"eyJ[A-Za-z0-9_-]+",
        "severity": "MEDIUM"
    },

    "private_key": {
        "regex": r"-----BEGIN PRIVATE KEY-----",
        "severity": "CRITICAL"
    },

    "password_keyword": {
        "regex": r"password\\s*=\\s*.+",
        "severity": "MEDIUM"
    }
}


def scan_content(content: str):

    findings = []

    for rule_name, rule in patterns.items():

        matches = re.findall(rule["regex"], content)

        if matches:
            findings.append({
                "type": rule_name,
                "severity": rule["severity"],
                "matches_found": len(matches),
                "sample": matches[0]
            })

    return findings
