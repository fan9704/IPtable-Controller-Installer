import platform
import subprocess
import re

from src.interface.config import Config
from rich import print
from rich.prompt import Prompt



def get_configs()->Config:
    HOST_IP = "127.0.0.1"
    IS_SINGLE_NODE = True
    MASTER_IP = "127.0.0.1"
    IS_MASTER = False

    ipv4_regex = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    def get_host_ip():
        global HOST_IP
        user_input = Prompt.ask("Enter HOST IP Address:")
        # IPv4 Rule
        
        if(bool(ipv4_regex.match(user_input))):
            HOST_IP = user_input
        else:
            print("[red]Invalid IP Address[/red]")
            get_host_ip()
    
    def get_master_ip():
        global MASTER_IP
        user_input = Prompt.ask("Enter MASTER IP Address:")
        # IPv4 Rule
        if(bool(ipv4_regex.match(user_input))):
            MASTER_IP = user_input
        else:
            print("[red]Invalid IP Address[/red]")
            get_master_ip()
    # --------------------------------
    # System Type Configuration
    # --------------------------------
    print("Getting IPC arguments")
    # OS
    print("Getting OS Version")
    print(f"[green]{platform.platform()}[/green]")
    # Network
    print("Getting Network Configuration")
    p = subprocess.Popen(['curl', 'icanhazip.com'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process_ip= p.stdout.readline()
    process_ip=process_ip.split(b"\n")[0]
    user_input = Prompt.ask(f"Is this IP for current machine? {process_ip.decode('utf-8')}", choices=["y", "n"], default="y")
    if(user_input == "y"):
        HOST_IP = process_ip.decode("utf-8")
    else:
        get_host_ip()
    # Is Single Node
    user_input = Prompt.ask("Single Node mode?", choices=["y", "n"], default="y")
    if(user_input == "n"):
        # Is Cluster Mode
        IS_SINGLE_NODE = False
        user_input = Prompt.ask("Is this machine a Master Node?",choices=["y", "n"], default="y")
        if(user_input == "y"):
            # Master Node
            IS_MASTER = True
            MASTER_IP = HOST_IP
        else:
            # Slave Node
            get_master_ip()
    else:
        # Single Node
        MASTER_IP = HOST_IP
        IS_MASTER = True
    # --------------------------------
    # Infra Config
    # --------------------------------
    # MongoDB Configuration
    MONGO_DB_HOST="127.0.0.1"
    MONGO_DB_USERNAME="test"
    MONGO_DB_PASSWORD="123456"
    MONGO_DB_DATABASE="network"
    MONGO_DB_PORT=27017
    # Mongo Express Configuration
    MONGO_EXPRESS_EXPORT_PORT=8081
    MONGO_EXPRESS_USERNAME="test"
    MONGO_EXPRESS_PASSWORD="123456"
    # Elasticsearch Configuration
    ELASTICSEARCH_HOST=MASTER_IP
    # RabbitMQ Configuration
    RABBIT_MQ_ENABLED=True
    RABBIT_MQ_HOST=MASTER_IP
    RABBIT_MQ_PORT=5672
    RABBIT_MQ_USERNAME="guest"
    RABBIT_MQ_PASSWORD="guest"
    
    config:Config = {
        "HOST_IP": HOST_IP,
        "IS_SINGLE_NODE": IS_SINGLE_NODE,
        "MASTER_IP": MASTER_IP,
        "IS_MASTER": IS_MASTER,
        # Mongo Configuration
        "MONGO_DB_HOST": MONGO_DB_HOST,
        "MONGO_DB_DATABASE":MONGO_DB_DATABASE,
        "MONGO_DB_USERNAME": MONGO_DB_USERNAME,
        "MONGO_DB_PASSWORD": MONGO_DB_PASSWORD,
        "MONGO_DB_PORT": MONGO_DB_PORT,
        # Mongo Express Configuration
        "MONGO_EXPRESS_EXPORT_PORT": MONGO_EXPRESS_EXPORT_PORT,
        "MONGO_EXPRESS_USERNAME": MONGO_EXPRESS_USERNAME,
        "MONGO_EXPRESS_PASSWORD": MONGO_EXPRESS_PASSWORD,
        # Elasticsearch Configuration
        "ELASTICSEARCH_HOST": ELASTICSEARCH_HOST,
        # RabbitMQ Configuration
        "RABBIT_MQ_ENABLED": RABBIT_MQ_ENABLED,
        "RABBIT_MQ_HOST": RABBIT_MQ_HOST,
        "RABBIT_MQ_PORT": RABBIT_MQ_PORT,
        "RABBIT_MQ_USERNAME": RABBIT_MQ_USERNAME,
        "RABBIT_MQ_PASSWORD": RABBIT_MQ_PASSWORD,
    }

    print("[bold green]Here is the Configuration[/bold green]")
    for config_name,value in config.items():
        print(f"{config_name} : {value}")
    user_input = Prompt.ask("Is this configuration correct?", choices=["y", "n"], default="y")
    if user_input == "n":
        print("[red]Please Retry[/red]")
        get_configs()
    else:
        print("[green]Configuration Completed[/green]")
    return config