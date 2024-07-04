import logging
import os

from rich import print
from rich.prompt import Prompt

def set_environment_variables(config: dict):
    print("Setting Environment Variables...")
    os.environ["HOST_IP"] = config["HOST_IP"]
    # MongoDB Configuration
    os.environ["MONGO_DB_HOST"] = config["MONGO_DB_HOST"]
    os.environ["MONGO_DB_DATABASE"] = config["MONGO_DB_DATABASE"]
    os.environ["MONGO_DB_USERNAME"] = config["MONGO_DB_USERNAME"]
    os.environ["MONGO_DB_PASSWORD"] = config["MONGO_DB_PASSWORD"]
    os.environ["MONGO_DB_PORT"] = str(config["MONGO_DB_PORT"])
    # Mongo Express Configuration
    os.environ["MONGO_EXPRESS_EXPORT_PORT"] = str(config["MONGO_EXPRESS_EXPORT_PORT"])
    os.environ["MONGO_EXPRESS_USERNAME"] = config["MONGO_EXPRESS_USERNAME"]
    os.environ["MONGO_EXPRESS_PASSWORD"] = config["MONGO_EXPRESS_PASSWORD"]
    # Elasticsearch Configuration
    os.environ["ELASTICSEARCH_HOST"] = config["ELASTICSEARCH_HOST"]
    # RabbitMQ Configuration
    os.environ["RABBIT_MQ_ENABLED"] = str(config["RABBIT_MQ_ENABLED"])
    os.environ["RABBIT_MQ_HOST"] = config["RABBIT_MQ_HOST"]
    os.environ["RABBIT_MQ_PORT"] = str(config["RABBIT_MQ_PORT"])
    os.environ["RABBIT_MQ_USERNAME"] = config["RABBIT_MQ_USERNAME"]
    os.environ["RABBIT_MQ_PASSWORD"] = config["RABBIT_MQ_PASSWORD"]
    print("[green]Environment Variables Setup Completed[/green]")

def application_package_install():
    # curl net-tools docker docker-compose git

    # Check Host CPU Architecture00
    pass