import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        exec_time = end_time - self.start_time
        print("time_1:", exec_time)

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    exec_time = end_time - start_time
    print("time_2:", exec_time)

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(2.2)
    with cm_timer_2():
        time.sleep(4.4)