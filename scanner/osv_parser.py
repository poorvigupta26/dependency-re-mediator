from models import Vulnerability

def parse_vulns(vuln_json):
    summary = (
        vuln_json.get("summary")
        or vuln_json.get("details")
        or "No Description Available."
    )

    aliases = vuln_json.get("aliases",[])

    return Vulnerability(
        id=vuln_json.get("id"),
        summary=summary,
        aliases=aliases
    )