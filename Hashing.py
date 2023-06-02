class HashTable:
    def __init__(self):

        self.table = [None]*10000000000001

    def hash_function(word):
        sum = 0
        for char in word:
            sum += ord(char)
            hash = sum % 1000000
            return hash

    def insert(self, key, value):
        hash = self.hash_function(key)
        if self.table[hash]:
            print(f"The key {key} already exists, if you want to update it, call the update() function, otherwise, change your key")
        else:
            self.table[hash] = value
            return value

    def get(self, key):
        hash = self.hash_function(key)
        if self.table[hash]:
            return self.table[hash]

    def update(self, key, value):
        hash = self.hash_function(key)
        self.table[hash] = value


