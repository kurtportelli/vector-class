class Vector:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def __str__(self):
        return '(' + ','.join([str(num) for num in self.numbers]) + ')'
        
    def equals(self, vector):
        return True if self.numbers == vector.numbers else False
        
    def add(self, vector):
        if len(self.numbers) != len(vector.numbers):
            raise Exception
        
        return Vector([a + b for a, b in list(zip(self.numbers, vector.numbers))])
        
    def subtract(self, vector):
        if len(self.numbers) != len(vector.numbers):
            raise Exception
        
        return Vector([a - b for a, b in list(zip(self.numbers, vector.numbers))])
        
    def dot(self, vector):
        if len(self.numbers) != len(vector.numbers):
            raise Exception
        
        return sum([a * b for a, b in list(zip(self.numbers, vector.numbers))])
        
    def norm(self):
        import math
        
        return math.sqrt(sum([a ** 2 for a in self.numbers]))
