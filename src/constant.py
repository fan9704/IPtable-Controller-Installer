import os

from pathlib import Path


PROJECT_PATH = Path(os.getcwd())

GITHUB_BASE_URL: str = "https://github.com/fan9704/"

MASTER_PROJECT_NAME: str = "IPtable-Controller-Master-Backend"
MASTER_PROJECT_URL: str = f"{GITHUB_BASE_URL}{MASTER_PROJECT_NAME}.git"
MASTER_PROJECT_DIR: str = f"{os.path.join(PROJECT_PATH,MASTER_PROJECT_NAME)}"
MASTER_FRONTEND_PROJECT_NAME: str = "IPtable-Controller-Master-Frontend"
MASTER_FRONTEND_PROJECT_URL: str = (
    f"{GITHUB_BASE_URL}{MASTER_FRONTEND_PROJECT_NAME}.git"
)

SLAVE_PROJECT_NAME: str = "IPtable-Controller-Backend"
SLAVE_PROJECT_URL: str = f"{GITHUB_BASE_URL}{SLAVE_PROJECT_NAME}.git"
SLAVE_PROJECT_DIR: str = f"{os.path.join(PROJECT_PATH,SLAVE_PROJECT_NAME)}"
SLAVE_FRONTEND_PROJECT_NAME: str = "IPtable-Controller-Frontend"
SLAVE_FRONTEND_PROJECT_URL: str = f"{GITHUB_BASE_URL}{SLAVE_FRONTEND_PROJECT_NAME}.git"
