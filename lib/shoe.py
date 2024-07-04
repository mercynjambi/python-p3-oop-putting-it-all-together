#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = None
        self.size = size
        self._condition = "Used"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    @property
    def condition(self):
        return self._condition
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"