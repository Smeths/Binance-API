from time import time

# dummy data for experimentation would be set by api
OPrice = [100,150,230,40,130]
CPrice = [150,230,40,130,70]
OPriceRead = [0,0,0,0,0]
CPriceRead = [0,0,0,0,0]

# abstractions: total trade interval, trade interval, time discretisation
#
# trade interval: opening  price read the start, closing price read at the end 
#
# total trade interval: the time measure in second over which the algorithm will continually run secs
#
# time discretisation: the api can't be called at "every instant", this is a denial of service attack
# so the time discretisation represents the interval unit of time that must passed between each
# iteration of the algorithm. The algorithm will run based on a "time count". The time count
# will increment every after a set period and parameter such as trading interval will be
# set according to the time count

# debug options
Debug = True

# total trade interval
strTime = time()
totTrdPeriod = 65 # time is secs

# time discretisation
tmDisTS = 1 # time step in secs. (Time discretisation, one mu 
tmDisnTS = 0 # number of time steps
tmDisPrevTime = time()

# trade interval
trdIntCount = 0 # the total number of trade intervals that have passed
trdIntTS = 15 # number of time steps per trading interval
trdIntOpen = True # flag to indicate the start of a trading interval

if Debug:
   print("Start time: " + str(strTime))
   
# implement total trading interval   
while time() - strTime < totTrdPeriod:
# implement time discretisation
    if time() - tmDisPrevTime > tmDisTS:
# implement trading intervals
        if trdIntOpen:
            trdIntOpen = False
            # to be replaced by api call
            OPriceRead[trdIntCount] = OPrice[trdIntCount]
            trdIntStrnTS = tmDisnTS            
        if trdIntCount > 0:
            if Debug:
                print("trading interval parameters")
                print("number of trading intervals: " + str(trdIntCount))
                print("one or more trading interval has passed implement trading logic")
                print("Current opening price: " + str(OPriceRead[trdIntCount]))
                print("Previous opening price: " + str(OPriceRead[trdIntCount-1]))
                print("Previous closing price: " + str(CPriceRead[trdIntCount-1])) 
        if tmDisnTS - trdIntStrnTS > trdIntTS: 
            trdIntOpen = True
            # to be replaced by api call
            CPriceRead[trdIntCount] = CPrice[trdIntCount] 
            trdIntCount = trdIntCount + 1
# updating time discretisation parameters        
        if Debug:
            print("time discretisation parameters")
            print("time: " + str(time()))
            print("Number of time steps: " + str(tmDisnTS))
            print("Start time of previous time step: " + str(tmDisPrevTime))
        tmDisnTS = tmDisnTS + 1    
        tmDisPrevTime = time()
    
    
    
    




