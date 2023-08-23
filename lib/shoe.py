#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand="Adidas", size="20"):
        self.brand = brand
        self.size = size
    
    def get_brand(self):
        return self.brand
    
    def get_shoe_size(self):
        return self.size
    
    def set_size(self, size):
        if isinstance(size, int):
            self.size = size
        else:
             print("size must be an integer")
    
    shoe_size = property(get_shoe_size, set_size)
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

