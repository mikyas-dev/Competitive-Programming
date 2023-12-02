class MyHashMap:
    def __init__(self):
        self.capacity = 10000
        self.hashMap = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        index = key % self.capacity
        if self.hashMap[index] is None:
            self.hashMap[index] = []
        for pair in self.hashMap[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hashMap[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % self.capacity
        if self.hashMap[index] is not None:
            for pair in self.hashMap[index]:
                if pair[0] == key:
                    return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.capacity
        if self.hashMap[index] is not None:
            for pair in self.hashMap[index]:
                if pair[0] == key:
                    self.hashMap[index].remove(pair)
                    return
