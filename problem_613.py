"""
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
"""


class PrefixMapSum:
    def __init__(self):
        self.dictionary = {}

    def insert(self, key: str, value: int):
        self.dictionary[key] = value

    def sum(self, prefix: str) -> int:
        count = 0
        for key, value in self.dictionary.items():
            if prefix in key:
                count += value
        return count


mapsum = PrefixMapSum()

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3
print(mapsum.sum("col") == 3)

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
print(mapsum.sum("col") == 5)
