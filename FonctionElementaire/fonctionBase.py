from collections import Counter

from outils import isConstant

global cte
cte = (float,int)

class ordre1:
    def __init__(self, value:list[tuple]) -> None:
        self.values, self.cte = self.reduce_init(value) 
        self.ordre = 'ordre1'
        self.isConstant = isConstant(list(self.values))
    
    def __add__(self, added):
        self.values += Counter({added:1})
        return self
    
    def __iadd__(self, added):
        self.values += Counter({added:1})
        return self
    
    def __str__(self):
        result = ""
        for key, value in dict(self.values).items():
            result += f"{value}*{key} + "
        return result + str(self.cte)
    
    def reduce_init(self, values:list[tuple]):
        constant = 0
        result = Counter({})
        for key, value in values:
            if value == 0 or key == 0: continue
            if type(key) in cte:
                constant += key * value
                continue
            result.update({key:value})
        return result, constant

class ordre2:
    def __init__(self, value:list[tuple]) -> None:
        self.values, self. cte = self.reduce_init(value)
        self.ordre = 'ordre2'
        self.isConstant = isConstant(list(self.values))

    
    def __mul__(self, timed):
        self.values += Counter({timed:1})
        return self
    
    def __imul__(self, timed):
        self.values += Counter({timed:1})
        return self
    
    def __str__(self):
        result = ""
        for key, value in dict(self.values).items():
            if value < 0:
                result += f"1/{key}^{-value} * "
            else:
                result += f"{key}^{value} * "
        return result + str(self.cte)
    
    def reduce_init(self, values:list[tuple]):
        constant = 1
        result = Counter({})
        for key, value in values:
            if value == 0: return Counter({}), 0
            if value == 1 or key == 0: continue
            if type(key) in cte:
                constant *= key ** value
                continue
            result.update({key:value})
        return result, constant

