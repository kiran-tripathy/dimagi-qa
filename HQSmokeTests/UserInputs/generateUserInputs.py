import random
import string

chars = string.ascii_lowercase + string.digits
random_string = ''.join(random.choices(chars, k=6))


def fetch_random_string():
    return random_string
