import subprocess

from rich import print
from rich.prompt import Prompt

SLAVE_PROJECT_NAME = "IPtable-Controller-Backend"
SLAVE_PROJECT_URL = f"https://github.com/fan9704/{SLAVE_PROJECT_NAME}.git"


def set_slave_node(config:dict):
    print("Setting Slave Node")
    # Backend
    p = subprocess.Popen(["git","clone",SLAVE_PROJECT_URL])
    p.wait()
    
    p = subprocess.Popen(["cd",SLAVE_PROJECT_NAME,"&&","docker-compose","up","-d"])
    p.wait()
    # TODO: Connect to Mongo and Create User

    print("[green]Slave Node Setup Completed[/green]")
    # Frontend
    # TODO: Setup Frontend