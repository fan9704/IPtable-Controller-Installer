from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError,ConfigurationError,OperationFailure
from src.interface.config import Config
from rich import print

def create_mongo_user(config:Config):
    MONGO_DB_HOST = config.get("MONGO_DB_HOST","127.0.0.1")
    MONGO_DB_DATABASE = config.get("MONGO_DB_DATABASE","network")
    MONGO_DB_USERNAME = config.get("MONGO_DB_USERNAME","test")
    MONGO_DB_PASSWORD = config.get("MONGO_DB_PASSWORD","123456")
    try:
        client = MongoClient(f'mongodb://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}/{MONGO_DB_DATABASE}?retryWrites=true&w=majority')
        user_script ={
        "user": MONGO_DB_USERNAME,
        "pwd": MONGO_DB_PASSWORD,
            "roles": [
                {"role": 'readWrite', db: MONGO_DB_DATABASE, "collection": MONGO_DB_DATABASE},
                {"role": 'readWrite', db: MONGO_DB_DATABASE},
                {"role": 'readWrite', db: 'admin'},
                { "role": "userAdminAnyDatabase", db: "admin" }
            ]
        }
        db = client['admin']
        db.command("createUser", user_script)
        # db_list = ["admin",MONGO_DB_DATABASE]
        # for db_name in db_list:
        #     db = client[db_name]
        #     users_collection = db['users']
        #     user = {"username": MONGO_DB_USERNAME, "password": MONGO_DB_PASSWORD}
        #     users_collection.insert_one(user)
        #     print(f"[green]Inserted User [bold]{MONGO_DB_USERNAME}[/bold] with DB: {db}[/green]")
    except ConfigurationError as e:
        print(f"[red]Mongo Configuration Error: {e}[/red]")
    except DuplicateKeyError as e:
        print(f"[red]User Already Exists: {e}[/red]")   
    except OperationFailure as e:
        print(f"[red]Operation Failure: {e}[/red]")
    except ConnectionError as e:
        print(f"[red]Connection Error: {e}[/red]")

if __name__ == "__main__":    
    config = {
        # Mongo Configuration
        "MONGO_DB_HOST": "127.0.0.1",
        "MONGO_DB_DATABASE":"network",
        "MONGO_DB_USERNAME": "test",
        "MONGO_DB_PASSWORD": "123456",
        "MONGO_DB_PORT": 27017,
    }
    create_mongo_user(config)