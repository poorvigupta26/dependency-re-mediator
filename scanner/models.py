from dataclasses import dataclass

@dataclass 
class Dependency:
    name: str
    version : str

@dataclass
class Vulnerability:
    id: str
    package: str
    current_version: str
    summary: str
    severity: str | None
    aliases: list[str]
    fixed: list[str]
    recommended: str | None

@dataclass
class RemediationAction:
    package: str
    current_version: str
    recommended_fix: str
    vulnerability: list[str]




