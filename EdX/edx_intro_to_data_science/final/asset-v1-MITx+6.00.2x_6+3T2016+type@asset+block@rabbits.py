import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    p=1-CURRENTRABBITPOP/float(MAXRABBITPOP)
    temp_pop=CURRENTRABBITPOP
    for i in range(CURRENTRABBITPOP):
        if random.random()<=p:
            temp_pop+=1
    CURRENTRABBITPOP=temp_pop
        

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    p=CURRENTRABBITPOP/float(MAXRABBITPOP)
    temp_pop=CURRENTFOXPOP
    for i in range(CURRENTFOXPOP):
        if random.random()<=p:
            if random.random()<=1/3:
                temp_pop+=1
            if CURRENTRABBITPOP>10:
                CURRENTRABBITPOP-=1
        elif random.random()<=0.9:
            if temp_pop>10:
                temp_pop-=1  
    CURRENTFOXPOP=temp_pop
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations=[]
    fox_populations=[]
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return(rabbit_populations,fox_populations)
