import subprocess
import os

def launch_prompt(path : str):
    if os.path.exists(path):
        subprocess.Popen([path],cwd=os.path.expanduser("~"))
    else:
        raise Exception("program path has not been found at " + path)
