# Umutcan CEYHAN  260201003
# Egg problem algorithm 
# part1
# It returns the minimum number of trials with given floor (H) and egg amount (N)
def minNumOfTrials(H,N):
    min = 999
    if(H == 1):         #BASE CASE 1
        return 1    
    if (N == 1):        #BASE CASE 2
        return H
    if (N == 0 or H == 0):  #BASE CASE 3 and 4
        return 0
    for i in range(1, H + 1):               #finding whole possibilities that can occur for every number 1 to H 
                    #Egg breaks               #Egg no breaks
        inc = max(minNumOfTrials(i-1,N-1),minNumOfTrials(H-i,N))    # taking maximum value for every number 1 to H 
        if inc < min:                               
            min = inc                       # then finding minimum of them  
    return min + 1                  # finally adding +1 the first try.

#part2
# It returns the brute force method of trials with given floor (H) and egg amount (N)
def bfNumOfTrials(H,N):
    if(H==1):
        return 1
    if(H == 0):
        return 0
    if(N == 0):
        return 0 
    return 1 + bfNumOfTrials(H-1,N)

def main():
    # User inputs
    floor = int(input("Please enter a floor number: "))
    eggAmount = int(input("Please enter amount of eggs: "))
    # Simulation
    print("Solutions to egg problem")
    print("Brute Force Method")
    print("You must try " + str(bfNumOfTrials(floor,eggAmount)) +" times to find floor in worst case")
    print("Minimum Number of Trials")
    print("You must try at least " + str(minNumOfTrials(floor,eggAmount)) + " times to find floor in worst case")
main()