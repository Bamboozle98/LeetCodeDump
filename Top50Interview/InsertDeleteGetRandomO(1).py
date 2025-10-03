class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.list = []

    def insert(self, val):
        if val not in self.set:
            self.set.add(val)
            self.list.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            self.list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        random_val = random.choice(self.list)
        return random_val
