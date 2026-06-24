import requests
import pprint
from models import Vulnerability
from osv_parser import parse_vulns
# from packaging import version

def get_vulnerabilities(
    package_name,
    package_version
):
    payload = {
    "version":package_version,
    "package":{
        "name":package_name,
        "ecosystem":"PyPI"
    }
}
    response = requests.post("https://api.osv.dev/v1/query", 
                            json=payload)

    data = response.json()

    vulnerabilities=[]
    for vuln in data.get("vulns", []):
        # if "GHSA" not in vuln["id"]:
        #     continue
        if not vuln:
            continue

        # pprint.pprint(vuln["affected"][0].get("ranges")[0].get("events")[1].get("fixed"))
        # print("\n\n\n\n\n\n")
        
        vulnerabilities.append(
            parse_vulns(vuln, package_name, package_version)
        )
        # vulnerabilities.append(
        #     Vulnerability(
        #         id=vuln.get("id"),
        #         summary=vuln.get("summary", vuln.get("details", "No information available.")),
        #         aliases=vuln.get("aliases",[])
        #     )
        # )
    return vulnerabilities
