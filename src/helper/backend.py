import os
import subprocess


from src.constant import MASTER_PROJECT_NAME,SLAVE_PROJECT_NAME,PROJECT_PATH
from src.helper.project import get_project_url

def set_up_backend(mode:str):
    if not (mode =="MASTER" or mode == "SLAVE"):
        print(f"[red] Mode:{mode} Setup Error by mode error[/red]")
    else:
        # Setup Mode Variables
        PROJECT_NAME=""
        if(mode == "MASTER"):
            PROJECT_NAME = MASTER_PROJECT_NAME
        elif(mode == "SLAVE"):
            PROJECT_NAME = SLAVE_PROJECT_NAME
        PROJECT_URL = get_project_url(PROJECT_NAME)
        # Clone and Host
        os.chdir(PROJECT_PATH)
        if(os.path.exists(PROJECT_NAME)):
            print(f"[red]{mode} Node Backend Already Exists[/red]")
        else:
            p = subprocess.Popen(['git','clone',PROJECT_URL])
            p.wait()
        os.chdir(f"{PROJECT_PATH}/{PROJECT_NAME}")
        p = subprocess.Popen(["docker-compose","up","-d"])
        p.wait()