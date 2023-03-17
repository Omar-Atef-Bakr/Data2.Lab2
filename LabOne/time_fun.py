import time

def timed_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute")
        return end_time - start_time
    return wrapper


# @timed_function
# def example_function():
#     # Your function code here
#     time.sleep(1) # Example delay
#
# example_function()


# newfun = timed_function(example_function)
# print(newfun())