from models import Vulnerability
from packaging import version

def parse_vulns(vuln_json, package, package_version):


    def extract_fixed_versions(vuln):
        fixed_versions = set()

        for affected in vuln.get("affected", []):
            for range_obj in affected.get("ranges", []):
                if range_obj.get("type") != "ECOSYSTEM":
                    continue
                for event in range_obj.get("events", []):
                    fixed = event.get("fixed")
                    if fixed:
                        fixed_versions.add(fixed)

        return list(fixed_versions)
    

    def safest_version(current, fixed):
        current = version.Version(current)
        candidates=[
            version.Version(v) for v in fixed
            if version.Version(v) > current
        ]
        if not candidates:
            return None
        
        return str(min(candidates))


    summary = (
        vuln_json.get("summary")
        or vuln_json.get("details")
        or "No Description Available."
    )

    severity= vuln_json.get("database_specific").get("severity", "unknown") if vuln_json.get("database_specific") is not None else None

    aliases = vuln_json.get("aliases",[])

    fixed = extract_fixed_versions(vuln_json)

    recommended = safest_version(package_version, fixed)

    return Vulnerability(
        id=vuln_json.get("id"),
        package= package,
        summary=summary,
        severity=severity,
        aliases=aliases,
        fixed= fixed,
        recommended=recommended
    )