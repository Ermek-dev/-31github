import hashlib
import product
from generator import Generator

class BronzeStrategy(Generator):
    def calculate(self):
        user_hash = "Bronze"
        calculate_md5_hash = hashlib.md5(user_hash.encode())
        if self.product.price<500:
            print(calculate_md5_hash.hexdigest())


