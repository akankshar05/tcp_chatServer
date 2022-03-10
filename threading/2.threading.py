import secrets
import time
start = time.perf_counter()


def do_something():
    print('sleeping 1 sec')
    time.sleep(1)
    print('done sleeping')

do_something()
do_something()

finish = time.perf_counter()
print(f'Finished in {round (finish - start, 2)} second(s)')

# result
# sleeping 1 sec
# done sleeping
# sleeping 1 sec
# done sleeping
# Finished in 2.01 second(s)

#///////////////////////////////////////
# when do_something function is called then => sleep for 1 sec
# 1 sec hone ke baad hi... doosra do_something chala ... => then again sleep 1 sec
# that's why total time = 2sec
