class HashTable:
    
    def __init__(self, capacity: int):
        self.hash = {}
        self.capacity = capacity

    def insert(self, key: int, value: int) -> None:
        self.hash[key] = value
        if len(self.hash) / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        if key in self.hash:
            return self.hash[key]
        return -1

    def remove(self, key: int) -> bool:
        if key in self.hash:
            del self.hash[key]
            return True
        return False

    def getSize(self) -> int:
        return len(self.hash)

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2
