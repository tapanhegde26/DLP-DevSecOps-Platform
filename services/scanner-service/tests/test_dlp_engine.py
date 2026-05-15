from dlp_scanner.services.dlp_engine import scan_content


def test_aws_key_detection():

    content = "AKIAIOSFODNN7EXAMPLE"

    findings = scan_content(content)

    assert len(findings) > 0