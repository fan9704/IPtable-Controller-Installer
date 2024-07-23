import os
import subprocess


from src.constant import SLAVE_FRONTEND_PROJECT_NAME, PROJECT_PATH,MASTER_FRONTEND_PROJECT_NAME
from src.helper.project import get_project_url

def set_up_frontend(mode:str):
    if not (mode =="MASTER" or mode == "SLAVE"):
        print(f"[red] Mode:{mode} Setup Error by mode error[/red]")
    else:
        # Setup Mode Variables
        PROJECT_NAME=""
        if(mode == "MASTER"):
            PROJECT_NAME = MASTER_FRONTEND_PROJECT_NAME
        elif(mode == "SLAVE"):
            PROJECT_NAME = SLAVE_FRONTEND_PROJECT_NAME
        PROJECT_URL = get_project_url(PROJECT_NAME)
        # Clone and Host
        os.chdir(PROJECT_PATH)
        if(os.path.exists(PROJECT_NAME)):
            print(f"[red]{mode} Node Frontend Already Exists[/red]")
        else:
            p = subprocess.Popen(['git','clone',PROJECT_URL])
            p.wait()
        os.chdir(f"{PROJECT_PATH}/{PROJECT_NAME}")
        # Build with Args and Up
        p = subprocess.Popen(["docker-compose","build"])
        p.wait()
        p = subprocess.Popen(["docker-compose","up","-d"])
        p.wait()
        print("[green]{mode} Node Frontend Setup Completed[/green")