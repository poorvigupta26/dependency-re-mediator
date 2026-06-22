from requirementParser import parse_reqs
from osv_client import get_vulnerabilities

deps = parse_reqs("../test-repos/vuln-repo/requirements.txt")

# def print_report(dependencies):
#     print("\nDependencies Found\n")

#     for dep in dependencies:
#         print(
#             f"{dep.name}=={dep.version}"
#         )

# print_report(deps)
# print("\n\n\n")

# get_vulnerabilities(deps[1].name, deps[1].version)

for dep in deps:
    vulns = get_vulnerabilities(dep.name, dep.version)
    print(f"found vulnerabilities in {dep.name}:")
    for vuln in vulns:
        print(f"{vuln.id} --> {vuln.summary}  -->  {vuln.aliases}")
    print("\n")


