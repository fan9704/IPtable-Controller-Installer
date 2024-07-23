import os

from rich import print
from src.config import get_configs
from src.env import set_environment_variables
from src.master import set_master_node
from src.slave import set_slave_node
from src.constant import PROJECT_PATH
from src.interface.config import Config
from src.dependencies.base import check_installation

def main():
    print(PROJECT_PATH)
    print("[blue]Starting IPC Installer[/blue]")
    config:Config = get_configs()

    # Set Environment Variables
    set_environment_variables(config)

    # Check Dependencies
    check_installation()

    # Set Master Node
    set_master_node(config)
    
    # Set Slave Node
    set_slave_node(config)

if __name__ == "__main__":
    main()