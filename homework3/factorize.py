from time import time
from multiprocessing import cpu_count, Pool, current_process

count_process = cpu_count()

def factorize(number):
    lst_res=[]
    for num in number:
        index=1
        lst_res_i=[]
        num_dividing_by_number(num)
        lst_res.append(lst_res_i)
    return lst_res
    raise NotImplementedError() 


def num_dividing_by_number(num):
    lst_res_i=[]
    for i in range(1,num+1):
        if not num%i:
            lst_res_i.append(i)
    return lst_res_i


if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060,5555, 6789087, 234578, 456789]
    start_time = time()
    lst_res=factorize(numbers)
    elapsed_time = time() - start_time
    print(f'factorize is done in {elapsed_time}')

    start_time1 = time()
    with Pool(processes=count_process) as pool:
            lst_res_multy = pool.map(num_dividing_by_number, numbers)
    elapsed_time1 = time() - start_time1
    print(f'factorize_multy is done in {elapsed_time1}')
   