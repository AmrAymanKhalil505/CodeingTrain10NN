import random
class Perceptron:
    def __init__(self,size):
        self.weights = []
        self.inputs =[]
        for i in range(size):
            self.weights.append(random.uniform(-1, 1))  
        self.inputs=[] 
    
    def guess (self):
        sum = 0.0;
        for i in range(len (self.weights)):
            sum += self.inputs[i]*self.weights[i]
        return self.activation (sum)  
    def activation (self,X):
         return 1 if X>=0  else -1
    
p = Perceptron(2)
p.inputs=[-1.0,.5]
print(p.guess())