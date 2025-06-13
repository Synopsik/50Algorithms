import asyncio
import time
import numpy

# TODO: Is there any way to calculate the space complexity as well as time? Need to add

class TestingTimer:
    def __init__(self):
        self.timer_start = None
        self.timer_stop = None
        self.results = []
    def start(self):
        self.timer_start = time.time()
    def stop(self, show=False):
        self.timer_stop = time.time()
        self.results.append(self.timer_stop - self.timer_start)
        if show:
            print(self.results[-1])
    def average_results(self):
        average = 0
        for result in self.results:
            average += result
        return average / len(self.results)
    def clear(self):
        self.results = []


def main():
    # Create timer
    timer = TestingTimer()
    # Do work and time it
    for x in range(10):
        timer.start()
        time.sleep(0.1) # Example work using sleep for 0.1 sec
        timer.stop()
    # Return an average from the list of results
    average_time = timer.average_results()
    # Print results
    print("\n" + str(average_time))
    # Clear out timer for more tests
    timer.clear()

if __name__ == "__main__":
    main()