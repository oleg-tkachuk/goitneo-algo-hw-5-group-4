class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)
                    return True
        return False


def main():
    items = {"apple": 10,
             "orange": 20,
             "banana": 30, }

    # Let's test our hash table
    H = HashTable(5)
    for key in items.keys():
        value = items.get(key)
        print(f"Homework 5 - Task 1 | Insert [{key} : {value}]")
        H.insert(key, value)

    # Delete the elements
    for key in items.keys():
        print(f"Homework 5 - Task 1 | Delete [{key}]")
        # Delete the element...
        H.delete(key)
        # And check, the result will be: None
        print(f"Homework 5 - Task 1 | Get [{key}] | Result: {H.get(key)}")


if __name__ == "__main__":
    print(f"Homework 5 - Task 1 | Starting...\n")
    main()
    print(f"\nHomework 5 - Task 1 | Done")
