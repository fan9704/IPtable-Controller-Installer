import os 
import subprocess

from rich import print
from src.constant import GITHUB_BASE_URL

def get_project_url(project_name:str)-> str:
    return f"{GITHUB_BASE_URL}{project_name}.git"


def clone_and_run_project(project_name:str):
    if(os.path.exists(project_name)):
        print("[red]Slave Node Already Exists[/red]")
    else:
        p = subprocess.Popen(["git","clone",get_project_url(project_name=project_name)])
        p.wait()
    
    p = subprocess.Popen(["cd",project_name,"&&","docker-compose","up","-d"])
    p.wait()