# Iptable-Controller-Installer

> FKT

---

![Logo](/doc/logo.png)

---

## Requirement

- Python 3.10^
- Poetry 1.8^
- Linux/Unix Like System
- docker/docker-compose

---

## Getting Started

### After Setup Complete 

Will add these environment variables to your machine

```shell
HOST_IP=127.0.0.1
# Mongo
MONGO_DB_HOST=127.0.0.1
MONGO_DB_DATABASE=network
MONGO_DB_USERNAME=test
MONGO_DB_PASSWORD=123456
MONGO_DB_PORT=27017
# Mongo Express
MONGO_EXPRESS_EXPORT_PORT=8081
MONGO_EXPRESS_USERNAME=test
MONGO_EXPRESS_PASSWORD=123456
# Elasticsearch
ELASTICSEARCH_HOST=127.0.0.1
# RabbitMQ
RABBIT_MQ_ENABLED=True
RABBIT_MQ_HOST=127.0.0.1
RABBIT_MQ_PORT=5672
RABBIT_MQ_USERNAME=guest
RABBIT_MQ_PASSWORD=guest
```

---

## Note

### Get current machine output IP

```shell
curl icanhazip.com
```

### Scan LocalNetwork All Machine IP

```shell
sudo apt update
sudo apt install arp-scan -y
sudo arp-scan --localnet
# OR
sudo apt install nmap -y
nmap -sn <LAN CIDR>
```

---

## Project-Link

- [IPC-Slave-Backend](https://github.com/fan9704/IPtable-Controller-Backend)
- [IPC-Slave-Frontend](https://github.com/fan9704/IPtable-Controller-Frontend)
- [IPC-Master-Backend](https://github.com/fan9704/IPtable-Controller-Master-Backend)
- [IPC-Master-Frontend](https://github.com/fan9704/IPtable-Controller-Master-Frontend)