from time import time
from joblib import Parallel, delayed

def add_process():
    sum_value = 0
    for i in range(10000):
        sum_value +=1
    return sum_value

if __name__ == "__main__":
    start = time()

    r = 0
    # for i in range(10000):
    #     r += add_process()

    r = Parallel(n_jobs=4, verbose=10)( [delayed(add_process)() for i in range(10000)])
    # Paralles(パラメータ)(delayed[(関数)(引数)for ループ条件)
    print(sum(r))

    print("{}".format(time() - start))