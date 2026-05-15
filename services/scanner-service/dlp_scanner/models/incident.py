from pydantic import BaseModel
from typing import List
from datetime import datetime


class Finding(BaseModel):
    type: str
    severity: str
    matches_found: int
    sample: str


class Incident(BaseModel):
    filename: str
    timestamp: datetime
    findings: List[Finding]
    overall_severity: str
