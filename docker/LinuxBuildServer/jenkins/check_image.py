#!/build/jenkins/pythonvenv/bin/python
import importlib
import sys

MODULE_LIST = ["pg8000", "numpy", "click", "matplotlib"]
IMP_ERROR = None
for m in MODULE_LIST:
    try:
        importlib.import_module(m)
    except ModuleNotFoundError:
        print(f"Failed to import {m}")
        IMP_ERROR = m
        break
    finally:
        print(f"{m} is installed and available.")

if IMP_ERROR is None:
    print("All modules are successfully imported.")
    # All is well no errors were detected.
    sys.exit(0)

# We did not succeed importing all modules
sys.exit(1)
