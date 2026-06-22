from models import Dependency

def parse_reqs(file_path):
    dependencies =[]

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
        
            if not line:
                continue

            if line.startswith("#"):
                continue

            if "==" not in line:
                continue

            name, version = line.split("==")

            dependencies.append(
                Dependency(
                    name= name.strip(),
                    version=version.strip()
                    )
            )
        return dependencies
