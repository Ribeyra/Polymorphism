KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75


# BEGIN (write your solution here)
class Rules:
    rules = {
        'kostrovok': lambda value: value + (value * 0.12),
        'book-king': lambda value: value * 75,
        None: lambda value: value
    }

    def get_rules(self):
        return self.rules

    @classmethod
    def normalize(self, key, value):
        unknown = self.rules[None]
        return self.rules.get(key, unknown)(value)

    def add_rule(self, rule):
        self.rules.update(rule)


def find_all_matching(data, filter={}):
    res = []
    for service in data:
        service_name = service['service']
        for hotel in service['hotels']:
            cost = Rules.normalize(service_name, hotel['cost'])
            if (
                cost > filter.get('min', 0) and
                cost < filter.get('max', float('inf'))
            ):
                res.append(
                    {
                        'hotel': {'cost': cost, 'name': hotel['name']},
                        'service': service_name
                    }
                )
    return res
# END


def find_the_cheapest_service(data, predicates=None):
    # BEGIN (write your solution here)
    filter = {} if predicates is None else predicates
    new_data = find_all_matching(data, filter)
    result = min(new_data, key=lambda x: x['hotel']['cost'])
    return result
    # END


data = [
  {'service': 'kostrovok', 'hotels': [{'name': '$JSInn', 'cost': 200}]},
  {'service': 'book-king', 'hotels': [{'name': '$phpInn', 'cost': 10}]}
]
# Цены на отели возвращаются уже в нормализованном виде
# возвращается массив отелей объединенных с именем сервиса из которого они
# извлекаются
hotel_infos = find_all_matching(data)
print(hotel_infos)
# [
#  {"hotel": {"cost": 224, "name": 'JSInn'}, "service": 'kostrovok'},
#  {"hotel": {"cost": 750, "name": '$phpInn'}, "service": 'book-king'}
# ]

data = [
  {'service': 'kostrovok', 'hotels': [{'name': '$JSInn', 'cost': 200}]},
  {'service': 'book-king', 'hotels': [{'name': '$phpInn', 'cost': 2}]}
]

print(find_the_cheapest_service(data))
# {'hotel': {'cost': 150, 'name':'$phpInn'}, 'service': 'book-king'}
print(find_the_cheapest_service(data, {'min': 200, 'max': 300}))
# {'hotel': {'cost': 224, 'name':'JSInn'}, 'service': 'kostrovok'}
