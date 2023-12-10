from abc import abstractmethod,ABC
import hashlib

class Generator(ABC):
    def __init__(self,honorary_code):
        self.honorary = honorary_code

    @abstractmethod
    def calculate(self):
        pass






