severity_order = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4
}


def calculate_overall_severity(findings):

    if not findings:
        return "LOW"

    highest = max(
        findings,
        key=lambda x: severity_order[x["severity"]]
    )

    return highest["severity"]
