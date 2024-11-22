class RandomizedSet:

    def __init__(self):
        self.list = []
        self.map = {}

    def search(self, val):
        return val in self.map

    def insert(self, val: int) -> bool:
        if not self.search(val):
            self.list.append(val)
            idx = len(self.list) - 1
            self.map[val] = idx
            return True

        return False
        
    def remove(self, val: int) -> bool:
        if self.search(val):
            idx = self.map[val]
            last = self.list[-1]
            self.list[idx] = last
            self.map[last] = idx
            self.list.pop()
            del self.map[val]
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()