import numpy as np
from matplotlib import pyplot as plt

def circle_eq(x):           #For experiments 5-6-7
    if x >= 1 and x <= 3:
        return np.sqrt(1-(x-2)**2)
    else:
        return 0
    
def sampleRejection():      #For experiments 5-6-7
    c = 2
    a = -1
    b = 4
    while True:
        u = np.random.rand()
        v = np.random.rand()
        x = (b-a)*u+a
        y = c*v
        if y <= circle_eq(x):
            return x

def experiment_1_2_3(number):      #I combined the first 3 experiment together because they are very familiar.
    numberOfValues = 0
    if(number == "1"):
        numberOfValues = 2
        bins = np.linspace(-1,3,1000)
    elif (number== "2"):
        numberOfValues = 10
        bins = np.linspace(0,10,1000)
    elif (number == "3"):
        numberOfValues = 50
        bins = np.linspace(15,35,1000)
    else:
        print("Wrong experiment number!")
    
    N = 100000
    sampleMean = 0
    standartDev = 0
    randomVariables = []
    sumsOfRandomVariables = []
    for i in range (N):
        sum = 0
        for i in range (numberOfValues):
            value = np.random.rand()
            randomVariables.append(value)
            sum += value
        sumsOfRandomVariables.append(sum)
        
    for i in range(N):
        sampleMean += sumsOfRandomVariables[i]
    sampleMean /= N
    
    for i in range(N):
         standartDev += ((sampleMean-sumsOfRandomVariables[i])**2)
    standartDev = (standartDev**0.5)/ (N**0.5)
    print("Experiment " + str(number))
    print("Sample mean is " + str(sampleMean))
    print("Sample standard deviation is " + str(standartDev))
    print(" ")
   
    if (number == "1"):              #According to the expected output file this histogram is only shown before the experiment1's histogram.
        plt.title('Histogram for generated random variables')
        plt.hist(randomVariables,100,density=True)
        plt.show()
        print(" ")
    
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sumsOfRandomVariables,100,density=True)
    plt.plot(bins,1/(standartDev*np.sqrt(2*np.pi))*np.exp(-(bins-sampleMean)**2/(2*standartDev**2)))
    plt.show()
    print(" ")
    

def experiment4():
    bins = np.linspace(36,50,1000)
    N = 100000
    sampleMean = 0
    standartDev = 0
    randomVariables = []
    sumsOfRandomVariables = []
    for i in range(N):
        sum = 0
        for i in range(100):
            if(sum < 40):
                value = np.random.uniform(0.5,1.5)
            else:
                value = np.random.uniform(-0.5,0.5)
            randomVariables.append(value)
            sum += value
        sumsOfRandomVariables.append(sum)
    for i in range(N):
        sampleMean += sumsOfRandomVariables[i]
    sampleMean /= N
    
    for i in range(N):
         standartDev += ((sampleMean-sumsOfRandomVariables[i])**2)
    standartDev = (standartDev**0.5)/ (N**0.5)
    print("Experiment 4")
    print("Sample mean is " + str(sampleMean))
    print("Sample standard deviation is " + str(standartDev))
    print()
   
    
    plt.title('Histogram for generated random variables')
    plt.hist(randomVariables,100,density=True)
    plt.show()
    print(" ")
    
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sumsOfRandomVariables,100,density=True)
    plt.plot(bins,1/(standartDev*np.sqrt(2*np.pi))*np.exp(-(bins-sampleMean)**2/(2*standartDev**2)))
    plt.show()
    print(" ")
    

    
def experiment_5_6_7(number):      #I combined the experiment 5,6 and 7 together because they are very familiar.
    numberOfValues = 0
    if(number == "5"):
        numberOfValues = 2
        bins = np.linspace(1,7,1000)
    elif (number== "6"):
        numberOfValues = 10
        bins = np.linspace(12,28,1000)
    elif (number == "7"):
        numberOfValues = 50
        bins = np.linspace(85,115,1000)
    else:
        print("Wrong experiment number!")
    
    N = 100000
    sampleMean = 0
    standartDev = 0
    randomVariables = []
    sumsOfRandomVariables = []
    
    for i in range (N):
        sum = 0
        for i in range(numberOfValues):
            value = sampleRejection()
            randomVariables.append(value)
            sum += value
        sumsOfRandomVariables.append(sum)
    for i in range(N):
        sampleMean += sumsOfRandomVariables[i]
    sampleMean /= N
    
    for i in range(N):
         standartDev += ((sampleMean-sumsOfRandomVariables[i])**2)
    standartDev = (standartDev**0.5)/ (N**0.5)
    print("Experiment " + str(number))
    print("Sample mean is " + str(sampleMean))
    print("Sample standard deviation is " + str(standartDev))
    print()
   
    if (number == "5"):       #According to the expected output file this histogram is only shown before the experiment5's histogram.
        plt.title('Histogram for generated random variables')
        plt.hist(randomVariables,100,density=True)
        plt.show()
        print(" ")
    
    plt.title('Histogram for sums of generated random variables')
    plt.hist(sumsOfRandomVariables,100,density=True)
    plt.plot(bins,1/(standartDev*np.sqrt(2*np.pi))*np.exp(-(bins-sampleMean)**2/(2*standartDev**2)))
    plt.show()
    print(" ")
        
      
    
experiment_1_2_3("1")
experiment_1_2_3("2")
experiment_1_2_3("3")
experiment4()
experiment_5_6_7("5")
experiment_5_6_7("6")
experiment_5_6_7("7")
