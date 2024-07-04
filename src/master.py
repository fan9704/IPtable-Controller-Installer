import subprocess

from rich import print
from rich.prompt import Prompt

MASTER_PROJECT_NAME = "IPtable-Controller-Master-Backend"
MASTER_PROJECT_URL = f"https://github.com/fan9704/{MASTER_PROJECT_NAME}.git"

def set_master_node(config:dict):
    print("Setting Master Node")
    if(config["IS_SINGLE_MODE"]):
        print("[red]Master Node is Disabled[/red]")
        
    else:
        # Backend
        print("[green]Master Node is Enabled[/green]")
        p = subprocess.Popen(["git","clone",MASTER_PROJECT_URL])
        p.wait()
        
        p = subprocess.Popen(["cd",MASTER_PROJECT_NAME,"&&","docker-compose","up","-d"])
        p.wait()
        print("[green]Master Node Setup Completed[/green]")
        # Frontend
        # TODO: Setup Frontend