# Entry Point -  it's dynamically typed (Python)

import os
import sys
import random
import asyncio
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from examples.challenges import fizzBuzz
from examples.challenges import palindrome
from examples.challenges import is_anagram
from examples.challenges import bubble_sort
from examples.challenges import factorial_iterative
from examples.challenges import factorial_recursive
from examples.challenges import etl_pipeline
from examples.challenges import build_sll
from examples.challenges import binary_search
from examples.challenges import two_sum
from examples.challenges import MinHeap

def estimate_big_o(input_sizes, times):
    growth_factors = []
    avg_growth = 0.000001
    for i in range(1, len(times)):
        if times[i - 1] != 0:
            growth_factors.append(times[i] / times[i - 1])
    avg_growth = sum(growth_factors) / len(growth_factors) if growth_factors else 0

    if avg_growth <= 1.5:
        return "0(1) - Constant" # Constant time
    elif avg_growth <= 2.0:
        return "O(log n) - Logarithmic" # Logarithmic time
    elif avg_growth <= 5.0:
        return "O(n) - Linear"     # Linear time
    elif avg_growth <= 20.0:
        return "O(n log n) - Quasi-linear" # Quasi-linear time
    else:
        return "O(n^2) - Exponential" # Quadratic time

def main():
    print(fizzBuzz(101))
    print("is 'level' palindrome? " + str(palindrome("level")))
    print("is 'rose' palindrome? " + str(palindrome("rose")))
    print("are 'listen' and 'silent' anagrams? " + str(is_anagram("listen", "silent")))
    print("are 'יהוה' and 'היוה' anagrams? " + str(is_anagram("יהוה", "היוה")))
    print("Bubble Sort([10,22,56,43,67,6,777]) = " + str(bubble_sort([10,22,56,43,67,6,777])))
    print("10! (Recursive) = " + str(factorial_recursive(10)))
    print("10! (Iterative) = " + str(factorial_iterative(10)))

    rawdata = "abgitz kryastn ngidksh btrtztg khkvtna iglpzk shkuxit brj shm kvd mlcto lolam vaed yahdvohnai"
    print("ETL Rawdata [" + rawdata  + "] \n ==> ETL Pipeline: " + str(etl_pipeline(rawdata)))

    rawdata = "אָ֑בְּגִ֣י־תֵּ֔ץ קָ֑רַע־שָׁ֔טַן נֶ֑גֶב־כָּ֔עַשׁ יִ֑תְגַּ֣ר־צַ֔ג בֶּֽטֶ֑נ־חַ֔קָּל שָֽׁקוֹ֑צִי־תֵּ֔ת עַ֑נְפַּ֣ע־צַ֔תּ"
    print("ETL Rawdata [" + rawdata + "] \n ==> ETL Pipeline: " + str(etl_pipeline(rawdata)))

    #rawdata = [23,34,45,56,42,24,14,33,66,77,8,9,100,1000,400,300]
    linked_list = build_sll(rawdata)

    print("Single Linked List seq. to_string() ==> " + str(linked_list))
    print("Single Linked List reversed. to_string() ==> " + str(linked_list.reverse()))

    times = []
    bin_arr = [12222,987*100,200202,232323,3434,45645,24,2*100,42,33,77,8,400,300,200,10,4,100*100]
    bin_arr.sort()
    input_sizes = []

    for n in bin_arr:
        target = 100
        input_sizes.append(len(bin_arr))  # All tests use the same array size
        bin_arr_explode = list(range(max(bin_arr)))
        start_time = time.time()
        found = binary_search(bin_arr_explode, target)
        end_time = time.time()
        times.append(end_time - start_time)
        print(f"Binary Search Time: {end_time - start_time:.6f} seconds.\n")
        print(f"Target found: {target}: {str(found)}")

    print("Big-O Time Complexity: " + estimate_big_o(input_sizes, times))

    #######################################################################

    nums = [1,40,0,100,10,10**100,2,3,4,5,66,677,7,8**9]
    print(f"Two numbers that add up 42 inside the following array {str(nums)} natural integers: {str(two_sum(nums, 42))}")

    my_heap = MinHeap()
    for n in nums:
        my_heap.push(n)

    while not my_heap.is_empty():
        n = my_heap.pop()
        print(f"My Heap: {str(n)}")

if __name__ == "__main__":
    main()