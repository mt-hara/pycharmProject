from functools import wraps
import time
def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elaped_time = time.time() - start
        print(f"{func.__name__}は{elaped_time}かかりました")
        return result
    return wrapper