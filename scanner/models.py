from dataclasses import dataclass

@dataclass 
class Dependency:
    name: str
    version : str

@dataclass
class Vulnerability:
    id: str
    package: str
    summary: str
    severity: str | None
    aliases: list[str]
    fixed: list[str]
    recommended: str | None

@dataclass
class Remediation:
    package: str
    current_version: str
    vulnerability: Vulnerability
    severity: str
    recommended_fix: str




