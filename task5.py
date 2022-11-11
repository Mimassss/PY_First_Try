
import string
import random

def get_random_password(num_qty, chars=string.ascii_letters + string.digits + string.punctuation) -> str:
        return ''.join(random.choice(chars) for _ in range(num_qty))



print(get_random_password(8))
