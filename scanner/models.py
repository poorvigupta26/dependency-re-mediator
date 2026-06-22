from dataclasses import dataclass

@dataclass 
class Dependency:
    name: str
    version : str

@dataclass
class Vulnerability:
    id: str
    summary: str
    aliases: list[str]