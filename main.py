from Animal import Animal
import matplotlib.pyplot as plt
from MaleAnimal import Male
from Female import Female
from environment import Environment
import random



def main():
    env = Environment()
    startChildRatio = 0.75 
    m =Male(1234, 2, startChildRatio, env, 2)
    env.addMale(m)
    f=Female(12345, 2, startChildRatio, env, 2)
    env.addFemale(f)
    env.addJuvenile(Female(12, 2, startChildRatio, env))
    env.addJuvenile(Male(123, 2, startChildRatio, env))

    initialRatio = env.getAverageRatio()
    ratios = []
    generations = []
    for i in range(20000): #need to run for at least 1000 generations to see results, for 10000 (suggested) takes 2-5 min to run
        #print("updating..." + "\n iteration: " + str(i))
        env.update()
        if i%100 ==0:
            ratios.append(env.getAverageRatio())
            generations.append(i)
        #print("current child ratio gene avg: " + str(env.getAverageRatio()))

    print("Initial Ratio: " + str(initialRatio) + ", Final Ratio: " + str(env.getAverageRatio()))

    plt.plot(generations, ratios)
    plt.xlabel("generation")
    plt.ylabel("population pct male offspring")
    plt.title("population genotype, sex ratio")
    plt.show()




    # ids = []   a check to see if any duplicate self.name generated
    # for i in env.getJuveniles():
    #     ids.append(i.getName())
    # ids.sort()
    # for i in ids:
    #     print(i)







main()
