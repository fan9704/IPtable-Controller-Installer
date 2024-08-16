import os

from rich import print
from src.interface.config import Config

def update_bashrc(variable_name, variable_value):
    # 讀取 .bashrc 文件
    with open('~/.bashrc', 'r+') as bashrc_file:
        lines = bashrc_file.readlines()
        
        # 檢查環境變數是否已存在
        for i, line in enumerate(lines):
            if line.strip().startswith(f'export {variable_name}'):
                # 如果存在，則覆蓋該行
                lines[i] = f'export {variable_name}={variable_value}\n'
                break
        else:
            # 如果不存在，則在文件末尾添加
            lines.append(f'export {variable_name}={variable_value}\n')

        # 替換文件內容
        bashrc_file.seek(0)
        bashrc_file.writelines(lines)
        bashrc_file.truncate()

def set_environment_variables(config: Config):
    print("[blue bold]Setting Environment Variables...[/blue bold]")

    update_bashrc("HOST_IP", config["HOST_IP"])
    update_bashrc("VITE_HOST_IP", config["HOST_IP"])
    # MongoDB Configuration
    update_bashrc("MONGO_DB_HOST", config["MONGO_DB_HOST"])
    update_bashrc("MONGO_DB_DATABASE", config["MONGO_DB_DATABASE"])
    update_bashrc("MONGO_DB_USERNAME", config["MONGO_DB_USERNAME"])
    update_bashrc("MONGO_DB_PASSWORD", config["MONGO_DB_PASSWORD"])
    update_bashrc("MONGO_DB_PORT", str(config["MONGO_DB_PORT"]))
    # Mongo Express Configuration
    update_bashrc("MONGO_EXPRESS_EXPORT_PORT", str(config["MONGO_EXPRESS_EXPORT_PORT"]))
    update_bashrc("MONGO_EXPRESS_USERNAME", config["MONGO_EXPRESS_USERNAME"])
    update_bashrc("MONGO_EXPRESS_PASSWORD", config["MONGO_EXPRESS_PASSWORD"])
    # Elasticsearch Configuration
    update_bashrc("ELASTICSEARCH_HOST", config["ELASTICSEARCH_HOST"])
    # RabbitMQ Configuration
    update_bashrc("RABBIT_MQ_ENABLED", str(config["RABBIT_MQ_ENABLED"]))
    update_bashrc("RABBIT_MQ_HOST", config["RABBIT_MQ_HOST"])
    update_bashrc("RABBIT_MQ_PORT", str(config["RABBIT_MQ_PORT"]))
    update_bashrc("RABBIT_MQ_USERNAME", config["RABBIT_MQ_USERNAME"])
    update_bashrc("RABBIT_MQ_PASSWORD", config["RABBIT_MQ_PASSWORD"])

    os.environ["HOST_IP"] = config["HOST_IP"]
    os.environ["VITE_HOST_IP"] = config["HOST_IP"]
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