import hashlib
from generator import Generator

class GoldStrategy(Generator):
    def calculate(self):
        user_hash = "Bronze"
        calculate_md5_hash = hashlib.md5(user_hash.encode())
        if self.product.price>=1000:
            print(calculate_md5_hash.hexdigest())
