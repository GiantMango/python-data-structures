class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0  # number of items (key-value pairs)

    def put(self, key, value):
        index = self.__hash_function(key)
        bucket = self.buckets[index]
        for i, item in enumerate(bucket):
            if item[0] == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])  # Resolve collision with chaining
        self.size += 1

    def get(self, key):
        index = self.__hash_function(key)
        bucket = self.buckets[index]

        for item in bucket:
            if item[0] == key:
                return item[1]
        raise KeyError(f"{key} not in hast table")

    def remove(self, key):
        # index = self.__hash_function(key)
        # if key == self.bucket[index][1]:
        #     removed =
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
        return self.size

    def __str__(self):
        text = []
        for i in range(self.capacity):
            text.append(f"    index {i}: {self.buckets[i]}")
        return "\n".join(text)

    def __hash_function(self, key):
        return sum([ord(x) for x in str(key)]) % self.capacity


if __name__ == "__main__":
    ht = HashTable()
    ht.put("name", "Taylor")
    ht.put("age", 29)
    ht.put("gae", 300)
    print(ht)
    ht.put("name", "Kevin")
    print("new hash table:\n", ht)
