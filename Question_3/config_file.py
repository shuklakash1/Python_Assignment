import configparser
import json
from flask import Flask
# import pymongo

app = Flask(__name__)

def get_configuration_dict(filename):
    try:
        config = configparser.ConfigParser()
        config.read(filename)
        configuration_dict = {}

        for section_name in config.sections():
            section_data = {}

            for parameter_name, parameter_value in config.items(section_name):
                section_data[parameter_name] = parameter_value

            configuration_dict[section_name] = section_data
        
        return configuration_dict
    
    except Exception as e:
        return {"error": str(e)}

# def save_congif_in_db():
#     config_data = get_configuration_dict('config.ini')

#     username = config_data["Database"]["username"]
#     password = config_data["Database"]["password"]
#     host = config_data["Database"]["host"]
#     port = config_data["Database"]["port"]

#     db_name = ""
#     db_collection = ""
    
#     mongo_connection_string = f"mongodb://{username}:{password}@{host}:{port}/?ssl=false" 

#     if "error" not in config_data:
#         json_data = json.dumps(config_data)

#         mongo_client = pymongo.MongoClient(mongo_connection_string)
#         coll = mongo_client[db_name][db_collection]

#         coll.insert_one(json_data)


@app.route('/config', methods=['GET'])
def get_config():
    config_data = get_configuration_dict('config.ini')
    if "error" in config_data:
        return config_data["error"], 500
    
    return json.dumps(config_data)


app.run(debug=True)

# save_congif_in_db()