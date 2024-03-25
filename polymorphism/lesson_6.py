"""
# проверяю пример из урока. Создаю класс гость и наследую от него класс
# пользователь.

class Guest:
    def __init__(self):
        self.name = 'Guest'
        self.articles = []

    @property
    def has_articles(self):
        return bool(self.articles)

    def get_name(self):
        return self.name

    def get_articles(self):
        return self.articles


guest = Guest()
print(guest.get_name())         # Guest
print(guest.has_articles)       # False
print(guest.get_articles())     # []


class User(Guest):
    def __init__(self, name):
        self.name = name
        self.articles = []

    def add_articles(self, title, text):
        self.articles = (title, text)


new_user = User('John Cena')
print(new_user.get_name())         # John Cena
print(new_user.has_articles)       # False
print(new_user.get_articles())     # []
new_user.add_articles('New article', 'Some text')
print(new_user.has_articles)       # True
print(new_user.get_articles())     # ('New article', 'Some text')

# guest.add_articles('New article', 'Some text')
# AttributeError: 'Guest' object has no attribute 'add_articles'. """


class Subscription():
    def __init__(self, subscription_plan_name):
        self.subscription_plan_name = subscription_plan_name

    def has_professional_access(self):
        return self.subscription_plan_name == 'professional'

    def has_premium_access(self):
        return self.subscription_plan_name == 'premium'


class FakeSubscription:
    def __init__(self, user):
        self.is_admin = user.is_admin()

    def has_professional_access(self):
        return self.is_admin

    def has_premium_access(self):
        return self.is_admin


class User():
    def __init__(self, email, current_subscription=None):
        self.email = email
        # BEGIN (write your solution here)
        if current_subscription is None:
            current_subscription = FakeSubscription(self)
        self.current_subscription = current_subscription
        # END

    def get_current_subscription(self):
        return self.current_subscription

    def is_admin(self):
        return self.email == 'rakhim@hexlet.io'


user1 = User('vasya@email.com', Subscription('premium'))
print(user1.get_current_subscription().has_premium_access())        # True
print(user1.get_current_subscription().has_professional_access())   # False

user2 = User('vasya@email.com', Subscription('professional'))
print(user2.get_current_subscription().has_premium_access())        # False
print(user2.get_current_subscription().has_professional_access())   # True

user3 = User('vasya@email.com')
print(user3.get_current_subscription().has_premium_access())        # False
print(user3.get_current_subscription().has_professional_access())   # False

user4 = User('rakhim@hexlet.io')    # администратор, проверяется по емейлу
print(user4.get_current_subscription().has_premium_access())        # True
print(user4.get_current_subscription().has_professional_access())   # True
