class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0  # number of items (key-value pairs)

    def put(self, key, value):
        index = self.__hash_function(key)
        self.buckets[index] = (key, value)
        self.size += 1

    def get(self, key):
        index = self.__hash_function(key)
        return self.buckets[index][1]

    def remove(self, key):
        pass

    def contains_key(self, key):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        text = []
        for i in range(self.capacity):
            text.append(f"index {i}: [{self.buckets[i]}]")
        return "\n".join(text)

    def __hash_function(self, key):
        return sum([ord(x) for x in str(key)]) % self.capacity


if __name__ == "__main__":
    ht = HashTable()
    ht.put("name", "Taylor")
    ht.put("age", 29)
    print(ht)
    name = ht.get("name")
    print(name)
