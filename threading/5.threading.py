import threading
import time
start = time.perf_counter()


def do_something():
    print('sleeping 1 sec')
    time.sleep(1)
    print('done sleeping')

threads=[]
for _ in range(10):
    t=threading.Thread(target= do_something)
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()

#this is same as ...runnig the code like 
#=>
#t1=threading..
# t1.start
# t2= threading..
# t2.start


# hame join bhi krna hoga isko 
#so to do this.. we can append each thread to a list... 
# and then join.
 




finish = time.perf_counter()
print(f'Finished in {round (finish - start, 2)} second(s)')

# result
# sleeping 1 sec
# sleeping 1 sec
# done sleepingdone sleeping

# Finished in 1.0 second(s)


