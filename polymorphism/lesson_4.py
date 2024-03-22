from pathlib import Path
import json

path = Path(__file__).parent / 'fixtures'
# path_to_configs = path.join(__dirname, '__fixtures__')
print(str(path))


class DatabaseConfigLoader:
    def __init__(self, path_to_dir):
        self.path = str(path_to_dir)

    def load(self, env):
        path_to_config = f"{self.path}/database.{env}.json"
        with open(path_to_config, "r") as data:
            config = self.parser(data)

        if 'extend' in config:
            new_env = config.pop('extend')
            new_config = self.load(new_env)
            for key, value in new_config.items():
                config.setdefault(key, value)
        return config

    def parser(self, data):
        config = json.load(data)
        return config
