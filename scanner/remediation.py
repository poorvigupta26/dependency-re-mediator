from models import RemediationAction
from collections import defaultdict
from packaging.version import Version


def build_remediation_plan(vulnerabilities):

    packaged_vulns = defaultdict(list)

    for vul in vulnerabilities:
        packaged_vulns[vul.package].append(vul)

    remediation_plan=[]
    
    for package, vulns in packaged_vulns.items():

        current_version = vulns[0].current_version

        target_version = str(max(
            Version(vuln.recommended)
            for vuln in vulns
            if Version(vuln.recommended) is not None
        ))

        vulnIDs = []
        for vul in vulns:
            vulnIDs.append(vul.id)

        action = RemediationAction(
            package=package,
            current_version=current_version,
            recommended_fix=target_version,
            vulnerability=vulnIDs,
        )

        remediation_plan.append(action)
    
    return remediation_plan

def print_remediation_report(remediation_plan):

   for action in remediation_plan:
        
        print(f"{action.package}: \n"
               f"current: {action.current_version} \n"
               f"target: {action.recommended_fix}\n"
               f"fixes:\n"
               f"{action.vulnerability}\n\n\n"
               )
        
def generate_remediated_requirements(remediation_plan, dependencies, path):
    upgrade_map = {}
    for action in remediation_plan:
        upgrade_map[action.package] = action.recommended_fix


    print(upgrade_map)   

    for dependency in dependencies:
        if dependency.name in upgrade_map:
            dependency.version = upgrade_map[dependency.name]

    with open(path+"/requirements.remediated.txt", "w+") as f:
        for dependency in dependencies:
            f.write(f"{dependency.name}=={dependency.version}\n")