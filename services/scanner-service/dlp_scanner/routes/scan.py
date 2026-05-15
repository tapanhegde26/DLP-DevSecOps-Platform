from fastapi import APIRouter, UploadFile, File
from datetime import datetime

from dlp_scanner.services.dlp_engine import scan_content
from dlp_scanner.utils.severity import calculate_overall_severity
from dlp_scanner.services.opensearch_service import store_incident

router = APIRouter()


@router.post("/scan/file")
async def scan_file(file: UploadFile = File(...)):

    content = await file.read()
    decoded = content.decode("utf-8", errors="ignore")

    findings = scan_content(decoded)

    severity = calculate_overall_severity(findings)

    incident = {
        "filename": file.filename,
        "timestamp": datetime.utcnow().isoformat(),
        "findings": findings,
        "overall_severity": severity
    }

    if findings:
        store_incident(incident)

    return {
        "incident": incident
    }
