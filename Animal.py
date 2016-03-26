import random
class Animal:

    def __init__(self, name,  fertility, childRatio, env, age=0):
        self.name = name
        self.childRatio = childRatio
        self.childs = []
        self.partner = None
        self.fertility = fertility
        self.gender = None
        self.age = age
        self.environment = env
        self.mutationRate = 0.05

    def addEnvironment(self, env):
        self.environment = env


    def setRatio(self, ratio):
        self.childRatio = ratio

    def getRatio(self):
        return self.childRatio
    def getChilds(self):
        return self.childs

    def getFertility(self):
        return self.fertility
    def getName(self):
        return self.name

    

   

    def older(self):
        self.age = 1 + self.age

    def mutate(self):
        if random.uniform(0,1)<self.mutationRate:
            if random.random()<0.5:
                self.childRatio += 0.04
            else:
                self.childRatio -=0.04
        if random.uniform(0,1)<0.0005:
            if random.random()<0.5:
                self.fertility += 1
            else:
                if self.fertility>=1:
                    self.fertility -=1
            
            

        



    def addChild(self, child):
        self.childs.append(child)

    def _eq_(self, other):
        return isinstance(other, self.__class__) and self.name == other.name


