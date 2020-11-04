import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    return "Done Sleeping"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]

    #Worse, but okay
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

    #Better
    #results = [executor.submit(do_something, sec) for sec in secs]

    #for f in concurrent.futures.as_completed(results):
        #print(f.result())

finish = time.perf_counter()

print(f'finished in {round(finish - start, 2)} second(s)')
