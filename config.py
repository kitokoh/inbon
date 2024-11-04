import json

class Config:
    def __init__(self, config_path="data.json"):
        self._config_data = self._load_config(config_path)

    def _load_config(self, config_path):
        try:
            with open(config_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Configuration file {config_path} not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the configuration file {config_path}.")
            return {}


    def get(self, key, default=None):
        return self._config_data.get(key, default)

    def __getattr__(self, item):
        return self.get(item)

# Instance globale de configuration
config = Config()
