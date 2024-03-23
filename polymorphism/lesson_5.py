from copy import deepcopy


class InMemoryKV:
    def __init__(self, value={}):
        self.value = deepcopy(value)

    def get_(self, key, default=None):
        return self.value.get(key, default)

    def set_(self, key, value):
        self.value[key] = value

    def unset_(self, key):
        self.value.pop(key)

    def to_dict(self):
        return deepcopy(self.value)


map = InMemoryKV({'key': 'value'})
# Получение значения по ключу
print(map.get_('key'))     # 'value'
print(map.get_('unknownkey'))  # None
# Получение значения и дефолт
print(map.get_('unknownkey', 'default value'))     # 'default value'
# Установка и обновление ключа
map.set_('key2', 'value2')
print(map.get_('key2'))    # 'value2'
# Удаление ключа
map.unset_('key2')
print(map.get_('key2'))    # None
map.set_('key', 'value')
# Возврат всех данных из базы (возвращается новый словарь)
print(map.to_dict())   # {'key': 'value'}


def swap_key_value(db_obj):
    data = db_obj.to_dict()
    keys = set()
    for key, value in data.items():
        keys.add(value)
        if key not in keys:
            db_obj.unset_(key)
        db_obj.set_(value, key)


map = InMemoryKV({'key': 10})
map.set_('key2', 'value2')
swap_key_value(map)
print(map.get_('key'))  # None
print(map.get_(10))     # 'key'
print(map.get_('value2'))   # 'key2'
