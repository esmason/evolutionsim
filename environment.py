from Animal import Animal
from MaleAnimal import Male
from Female import Female
import random

class Environment:
    def __init__(self):
        self.males = []
        self.females = []
        self.juveniles = []
        self.growUpAge = 2 #age animals start mating
        self.dieAge = 4 #age adult animals die
        self.maxPop = 400 #runs very slow if much above 1E3


    def addMale(self,m):
        self.males.append(m)
        m.addEnvironment(self)

    def addFemale(self,f):
        self.females.append(f)
    
    def addJuvenile(self,j):
        self.juveniles.append(j)
                
    def getMales(self):
        return self.males

    def getFemales(self):
        return self.females

    def getJuveniles(self):
        return self.juveniles

    def getNumMales(self):
        return len(self.getMales())

    def hasFemales(self):
        return len(self.females) > 0


    def getNumFemales(self):
        return len(getFemales())

    def getNumJuveniles(self):
        return len(getJuveniles())

    def removeAdult(self, a):
        if a.isFemale():
            self.females.remove(a)
        else:
            self.males.remove(a)
    def growUp(self, a):
        self.juveniles.remove(a)
        if a.isFemale():
            self.addFemale(a)
        else:
            self.addMale(a)


    def updateAnimalsAge(self):
        for a in self.males:
            a.older()
            if (a.age > self.dieAge):
                self.removeAdult(a)

        for a in self.females:
            a.older()
            if (a.age > self.dieAge):
                self.removeAdult(a)

        for a in self.juveniles:
            a.older()
            if (a.age==self.growUpAge):
                self.growUp(a)

    def removeJuvenile(self, j):
        self.juveniles.remove(j)
                
    def getFemalesNotTaken(self):
        notTaken=[]
        for f in self.females:
            if not f.getHasPartner():
                notTaken.append(f)
        return notTaken


    # maintains M/F/J ratio and randomly removes enough animals to keep total animals < maxPop
    def dieOff(self):
        total = len(self.getFemales()) + len(self.getMales()) + len(self.getJuveniles())
        percentFemale = len(self.getFemales())/total
        percentMale = len(self.getMales())/total
        percentJuvenile = len(self.getJuveniles())/total

        while len(self.getMales()) > round(percentMale*self.maxPop):

            self.removeAdult(random.choice(self.getMales()))
        while len(self.getFemales()) > (percentFemale*self.maxPop):
            self.removeAdult(random.choice(self.getFemales()))
        while len(self.getJuveniles()) > round(percentJuvenile*self.maxPop):
            self.removeJuvenile(random.choice(self.getJuveniles()))


            

    #invariants: total population less than maxPop, organisms in appropriate category for age, currently no organisms
    # have partners

    def update(self):

        self.updateAnimalsAge()
        males = self.getMales()
        for m in males:
            m.findPartner()

            if m.hasPartner():
                m.getPartner().setPartner(True) #to maintain 1-1 matingm, aka 'monogamy' each update
                m.mate()
                for c in m.getChilds():
                    self.addJuvenile(c)
                m.clearChilds()
            for m in males:
                m.setPartner(None)
        for f in self.getFemales():
            f.mutate()
            f.setPartner(False)

        if len(self.getFemales()) >100 and len(self.getMales())>100: #animals die when population gets too big
            self.dieOff()

    def getAverageRatio(self):
        sum = 0
        allAnimals =  self.getMales()+self.getFemales()+self.getJuveniles()
        for a in allAnimals:
            sum = sum + a.getRatio()
        return sum/len(allAnimals)









        
            
        
            
        
        
