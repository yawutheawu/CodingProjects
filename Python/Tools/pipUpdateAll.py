from importlib.metadata import distributions
import time
from subprocess import call

errors = []
packages = [dist.name for dist in distributions()]
print(f"{len(packages)} packages to check")
for i in packages:
    print("Getting " + i + " With " + "pip install --upgrade " + i)
    try:
        call("pip install --upgrade " + i, shell=True)
    except Exception as e:
        print("----------------------------------")
        errors.append(i)
        print(f"Error {e} on {i}")
        print("----------------------------------")
call("echo Read Errors:", shell = True)
call("echo " + " ".join(errors), shell = True)
time.sleep(5)   
