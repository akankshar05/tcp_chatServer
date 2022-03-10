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



finish = time.perf_counter()
print(f'Finished in {round (finish - start, 2)} second(s)')

# result
# sleeping 1 sec
# sleeping 1 sec Finished in 0.0 second(s)

# done sleeping done sleeping


