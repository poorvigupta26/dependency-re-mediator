from requirementParser import parse_reqs
from osv_client import get_vulnerabilities
from models import Remediation

deps = parse_reqs("../test-repos/vuln-repo/requirements.txt")

# def print_report(dependencies):
#     print("\nDependencies Found\n")

#     for dep in dependencies:
#         print(
#             f"{dep.name}=={dep.version}"
#         )

# print_report(deps)
# print("\n\n\n")

# vul = get_vulnerabilities(deps.name, deps.version)
# for v in vul:
#     print(v)
#     print("\n\n\n\n\n")
remediation_methods=[]
for dep in deps:
    vulns = get_vulnerabilities(dep.name, dep.version)
    for vul in vulns:
        remediation_methods.append(
            Remediation(
                package=dep.name,
                current_version=dep.version,
                vulnerability=vul,
                severity=vul.severity,
                recommended_fix=vul.recommended
            )
        )
    

for remediation in remediation_methods:
    print(remediation)
    print("\n\n\n\n")


