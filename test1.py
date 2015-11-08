__author__ = 'ykk'

from Crypto.Hash import SHA256


def hash_password(clear_password):
    return SHA256.new(clear_password).hexdigest()


def check_password(clear_password, password_hash):
    return SHA256.new(clear_password).hexdigest() == password_hash


if __name__ == "__main__":
    z = 'abv'
    a = hash_password('abv')
    c = len(a)*4
    print(c)
    print(a)
    print(check_password(z, a))