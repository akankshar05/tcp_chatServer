import time
start = time.perf_counter()


def do_something():
    print('sleeping 1 sec')
    time.sleep(1)
    print('done sleeping')


do_something()

finish = time.perf_counter()

print(f'Finished in {round (finish - start, 2)} second(s)')
