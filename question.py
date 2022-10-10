# random number generator

import random
class Question:
    def __init__(self):
        self.a = random.randint(1,99)
        self.b = random.randint(1,99)
        self.ops=['+','-']
        self.c=random.randint(0,1)
    
    def generate_ques(self):
        return(str(self.a)+self.ops[self.c]+str(self.b))
    
    def answer(self):
        if self.ops[self.c]=='+':
            return self.a + self.b
        else:
            return self.a - self.b