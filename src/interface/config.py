from typing import TypedDict

class Config(TypedDict):
    HOST_IP:str="127.0.0.1"
    IS_SINGLE_NODE:bool= True
    MASTER_IP:str = "127.0.0.1"
    IS_MASTER:bool = False
    # --------------------------------
    # Infra Config
    # --------------------------------
    # MongoDB Configuration
    MONGO_DB_HOST:str=HOST_IP
    MONGO_DB_USERNAME:str="test"
    MONGO_DB_PASSWORD:str="123456"
    MONGO_DB_DATABASE:str="network"
    MONGO_DB_PORT:int=27017
    # Mongo Express Configuration
    MONGO_EXPRESS_EXPORT_PORT:int=8081
    MONGO_EXPRESS_USERNAME:str="test"
    MONGO_EXPRESS_PASSWORD:str="123456"
    # Elasticsearch Configuration
    ELASTICSEARCH_HOST=MASTER_IP
    # RabbitMQ Configuration
    RABBIT_MQ_ENABLED=True
    RABBIT_MQ_HOST:str=MASTER_IP
    RABBIT_MQ_PORT:int=5672
    RABBIT_MQ_USERNAME:str="guest"
    RABBIT_MQ_PASSWORD:str="guest"