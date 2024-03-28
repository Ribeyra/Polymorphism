import hashlib
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits as ascii_digits,
    punctuation
)
import random


class PasswordBuilder:
    def __init__(self, passwordGenerator):
        self.passwordGenerator = passwordGenerator

    def build_password(self, len=10, options=[]):
        password = self.passwordGenerator.generate_password(len, options)
        m = hashlib.sha1()
        m.update(password.encode())
        digest = m.hexdigest()

        return {'password': password, 'digest': digest}


def generate_password(len, uppercase=False, digits=False, symbols=False):
    gen_pool = ascii_lowercase
    if uppercase:
        gen_pool += ascii_uppercase
    if digits:
        gen_pool += ascii_digits
    if symbols:
        gen_pool += punctuation
    return ''.join(random.choice(gen_pool) for _ in range(len))


class PasswordGeneratorAdapter:
    @staticmethod
    def generate_password(len, options):
        opt = {key: True for key in options}
        return generate_password(len, **opt)


builder = PasswordBuilder(PasswordGeneratorAdapter())

password_info = builder.build_password(10, ['uppercase', 'digits'])
print(password_info)
