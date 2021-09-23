class expr:
    pass


class times(expr):
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def __str__(self):
        return "(" + str(self.left) + " * " + str(self.right) + ")"
        
    def evaluate(self, env):
        return self.left.evaluate(env) * self.right.evaluate(env)
        

class plus(expr):
        
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def __str__(self):
        return "(" + str(self.left) + " + " + str(self.right) + ")"
        
    def evaluate(self, env):
        return self.left.evaluate(env) + self.right.evaluate(env)
    

class const(expr):
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    def evaluate(self, env):
        return self.val


class var(expr):
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def evaluate(self, env):
        return env[self.name]
        


expr1 = times(const(3), plus(var("y"), var("x")))
expr2 = plus(times(const(3), var("x")), var("y"))

env = {"x" : 2, "y" : 4}

print(expr1)
print(expr2)
