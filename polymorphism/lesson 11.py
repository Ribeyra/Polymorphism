import json
import yaml
import pathlib
import os


class Config:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.data = data

    def get_value(self, key):
        result = self.data[key]
        if isinstance(result, dict):
            return Config(result)
        return result


class JSONParser:
    # BEGIN (write your solution here)
    def __init__(self):
        pass

    @staticmethod
    def parser(raw_data):
        return json.loads(raw_data)
    # END


class YAMLParser:
    # BEGIN (write your solution here)
    def __init__(self):
        pass

    @staticmethod
    def parser(raw_data):
        return yaml.safe_load(raw_data)
    # END


PARSERS = {
    '.yaml': YAMLParser,
    '.yml': YAMLParser,
    '.json': JSONParser,
}


class ConfigFactory:
    def __init__(self):
        pass

    @staticmethod
    def read_file(path):
        with open(path) as file:
            raw_data = file.read()
        return raw_data

    @staticmethod
    def factory(path):
        file_ext = os.path.splitext(path)[-1]
        parser_class = PARSERS[file_ext]
        raw_data = ConfigFactory.read_file(path)
        data = parser_class.parser(raw_data)
        config = Config(data)
        return config


filepath = pathlib.Path('.').joinpath('fixtures', 'test.yml')

print(os.path.splitext(filepath)[-1])
