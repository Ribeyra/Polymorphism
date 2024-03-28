import json


class EqualityMixin:
    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.__dict__ == other.__dict__
        return False


class SerializeMixin:
    def serialize(self):
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize(cls, data):
        attr = json.loads(data)
        return cls(**attr)


class BaseUser:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class User(BaseUser, EqualityMixin, SerializeMixin):
    pass


""" u1 = User('Mike', 'mike@mail.com', 'foobar')
u2 = User('Mike', 'mike@mail.com', 'foobar')
u3 = User('Alice', 'alice@mail.com', 'verystrongpass')

print(u1 == u2)  # True
print(u1 == u3)  # False

u4 = BaseUser('Mike', 'mike@mail.com', 'foobar')
# миксин позволяет сравнивать лишь экземпляры одного и того же класса
print(u1 == u4)  # False """


u1 = User('Mike', 'mike@mail.com', 'foobar')
data = u1.serialize()
# {"name": "Mike", "email": "mike@mail.com", "password": "foobar"}

# метод deserialize должен возвращать новый объект
u2 = User.deserialize(data)

# аттрибуты равны
print(u1 == u2)  # True

# но объект создается новый
print(u1 is u2)  # False
