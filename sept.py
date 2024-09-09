
#LA-1

class hero:
    name = "layla"
    
mm = hero()
print(mm.name)

#LA-2

class hero: 
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
character = hero("layla", "marksman")
print(character.name, character.role)

#LA-3

class character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def describe(self):
        print(f" {self.name} is a {self.role} hero.")
        
ml = character("silong", "fighter")
ml.describe()

#LA-4

class character:
    def __init__(self, name, role):
        self.name = name
        self.role= role
        
    def __str__(self):
        return f" {self.name} is a {self.role} hero."
    
ml =character("zilong", "fighter")
print()

