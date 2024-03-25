"""
# модифицирую пример из урока

class User:
    def __init__(self, name):
        self.name = name


class Guest(User):
    def __init__(self):
        self.name = 'guest'


def say_hi(user):
    try:
        return f'Hello, {user.name}!'
    except AttributeError:
        return 'Who are you?'


new_user = User('John Cena')    # Hello, John Cena!
print(say_hi(new_user))
new_guest = Guest()
print(say_hi(new_guest))        # Hello, guest!
wrong_user = 'John Dow'
print(say_hi(wrong_user))       # Who are you? """


class User:
    def __init__(self, name):
        self.name = name
        # BEGIN (write your solution here)

        # END

    def get_name(self):
        return self.name

    # BEGIN (write your solution here)
    def is_user(self):
        return True
    # END


class Guest:
    def __init__(self):
        self.name = 'Guest'
        # BEGIN (write your solution here)

        # END

    def get_name(self):
        return self.name

    # BEGIN (write your solution here)
    def is_user(self):
        return False
    # END


def greet(user):
    if user.is_user():
        return f'Hello {user.name}!'
    return 'Nice to meet you Guest!'


guest = Guest()
print(greet(guest))  # 'Nice to meet you Guest!'

user = User('Tota')
print(greet(user))  # 'Hello Tota!'
