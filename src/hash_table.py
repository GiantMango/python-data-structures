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
        index = self.__hash_function(key)
        for i, item in enumerate(self.buckets[index]):
            if item[0] == key:
                removed = self.buckets[index].pop(i)
                self.size -= 1
                return removed[1]
        raise KeyError(key)

    def keys(self):
        re = []
        for bucket in self.buckets:
            for x in bucket:
                re.append(x[0])
        return re

    def values(self):
        re = []
        for bucket in self.buckets:
            for x in bucket:
                re.append(x[1])
        return re

    def items(self):
        re = []
        for bucket in self.buckets:
            for x in bucket:
                re.append(x)
        return re

    def contains(self, key):
        return self.__contains__(key)

    def __contains__(self, key):
        index = self.__hash_function(key)
        return key in [x[0] for x in self.buckets[index]]

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
    ht.remove("gae")
    print(ht)
    ht.remove("last")
