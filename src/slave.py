import os 
import time

from rich import print
from src.interface.config import Config
from src.constant import  PROJECT_PATH
from src.helper.mongo import create_mongo_user
from src.helper.backend import set_up_backend
from src.helper.frontend import set_up_frontend

def set_slave_node(config:Config):
    print("Setting Slave Node")
    os.chdir(PROJECT_PATH)
    
    # Backend
    set_up_backend("SLAVE")
    # Connect to Mongo and Create User
    time.sleep(3)
    create_mongo_user(config)
    print("[blue]Mongo DB Complete[/blue]")
    print("[green]Slave Node Backend Setup Completed[/green]")
    # Frontend
    os.chdir(PROJECT_PATH)
    set_up_frontend("SLAVE")
    # Frontend Setup Complete
    print("[green]Slave Node Frontend Setup Completed[/green]")
    print("[bold green]Slave Node Setup Completed[/bold green]")