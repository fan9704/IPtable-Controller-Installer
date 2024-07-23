import os

from rich import print
from src.interface.config import Config
from src.constant import PROJECT_PATH
from src.helper.backend import set_up_backend
from src.helper.frontend import set_up_frontend

def set_master_node(config:Config):
    print("Setting Master Node")
    if(config["IS_SINGLE_NODE"]):
        print("[red] Master Node is Disabled [/red]")
    else:
        # Backend
        set_up_backend("MASTER")
        print("[green]Master Node Backend Setup Completed[/green]")
        # Frontend
        os.chdir(PROJECT_PATH)
        set_up_frontend("MASTER")
        # Frontend Setup Complete
        print("[green]Master Node Frontend Setup Completed[/green]")
        print("[bold green]Master Node Setup Completed[/bold green]")