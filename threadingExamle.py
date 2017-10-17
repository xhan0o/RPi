import time
from threading import Thread


#Funciton to thread
def post(data):
  print time.time() #start time
  print data  #data transfer function
  time.sleep(5) #time delay
  print "Finished" + str(time.time()) #end time 
  return


#Main

for data in range(10): #loop for 10
    t = Thread(target=post, args=(data,)) #threading 
    t.start() #Start 
    print (data) 
