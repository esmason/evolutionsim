from Animal import Animal
from Female import Female
import random
class Male(Animal):
    def __init__(self, ID, fertility, childRatio, env, age=0):
        Animal.__init__(self, ID, fertility, childRatio, env, age)

        self.gender = 'm'
        self.partner=None

    def setPartner(self, p):
        self.partner = p

    def findPartner(self):
        if len(self.environment.getFemalesNotTaken())>0:

            self.partner = random.choice(self.environment.getFemalesNotTaken())
        else:
            self.partner = None

    def isFemale(self):
        return False

    def _eq_(self, other):
        return isinstance(other, self.__class__) and self.ID == other.ID
    def getPartner(self):
        return self.partner

    def hasPartner(self):
        return self.partner is not None

    #assumes male has a partner
    def mate(self):
        partnerRatio = self.partner.getRatio()
        newChildRatio = (partnerRatio + self.childRatio )/2.0
        ##TODO: add randomness to numchilds
        newFertility = int(round((self.fertility + self.partner.getFertility())/2))
        babies= newFertility
        if random.random()<0.1:
            if random.random()<0.5:
                babies+=1
            else:
                babies-=1

        self.mutate();

        if self.hasPartner():
            for i in range(babies):
                if random.random()<self.getRatio():
                    self.addChild(Male(random.random(), newFertility, newChildRatio, self.environment))#addrandomness

                else:
                    self.addChild(Female(random.random(), newFertility, newChildRatio, self.environment))

    def clearChilds(self):
        del self.childs[:]
                                  
                    
                    
                
        
        
        
            
