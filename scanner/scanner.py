from requirementParser import parse_reqs
from osv_client import get_vulnerabilities
from remediation import build_remediation_plan, print_remediation_report, generate_remediated_requirements

path = "../test-repos/vuln-repo"
deps = parse_reqs(path+"/requirements.txt")

print(deps)

for dep in deps:
    vulns = get_vulnerabilities(dep.name, dep.version)
    remediation_plan = build_remediation_plan(vulns)
    generate_remediated_requirements(remediation_plan, deps, path)
    
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
# remediation_methods=[]
# for dep in deps:
#     vulns = get_vulnerabilities(dep.name, dep.version)
#     for vul in vulns:
#         remediation_methods.append(
#             Remediation(
#                 package=dep.name,
#                 current_version=dep.version,
#                 vulnerability=vul,
#                 severity=vul.severity,
#                 recommended_fix=vul.recommended
#             )
#         )
    

# for remediation in remediation_methods:
#     print(remediation)
#     print("\n\n\n\n")


