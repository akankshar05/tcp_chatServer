import threading
import time
start = time.perf_counter()


def do_something():
    print('sleeping 1 sec')
    time.sleep(1)
    print('done sleeping')
t1 =threading.Thread(target= do_something)
t2 =threading.Thread(target= do_something)

t1.start()
t2.start()
t1.join()
t2.join()

# join method will make sure that the threadings complete before moving on to calculate finishing time
# join() is what causes the main thread to wait for your thread to finish. Otherwise, your thread runs all by itself.
# matlab jo main whole code ka thread chal rha wo..tba hi finish hoga jab aur saare threads finish ho gy honge  ..
# 

finish = time.perf_counter()
print(f'Finished in {round (finish - start, 2)} second(s)')

# result
# sleeping 1 sec
# sleeping 1 sec
# done sleepingdone sleeping

# Finished in 1.0 second(s)


