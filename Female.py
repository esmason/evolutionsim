from Animal import Animal
import random
class Female(Animal):
    def __init__(self, ID, fertility, childRatio, env, age=0):
        Animal.__init__(self, ID, fertility, childRatio, env, age)

        self.gender = 'f'
        self.hasaPartner = False;

    def getHasPartner(self):
        return self.hasaPartner

    #h must be boolean
    def setPartner(self, h):
        self.hasaPartner = h

    def isFemale(self):
        return True

    def _eq_(self, other):
        return isinstance(other, self.__class__) and self.ID == other.ID

    
    
