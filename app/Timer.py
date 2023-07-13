import time

class Timer:
    start_time = None

    @staticmethod
    def start_timer():
        return time.time()
    
    @staticmethod
    def stop_timer(start_timer):
        end_time = time.time()
        elapsed_time = end_time - start_timer
        return elapsed_time

