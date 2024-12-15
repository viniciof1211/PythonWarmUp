# Entry Point -  it's dynamically typed (Python)

import os
import sys
import random
import asyncio
import time
import csv
import traceback

import numpy as np

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
from examples.challenges import json_to_csv
from examples.challenges import harmony_sort

def estimate_big_o(input_sizes, times, k=None):
    input_sizes = np.array(input_sizes)
    times = np.array(times)
    # Input sizes & times must be positive and valid
    if len(input_sizes) < 2 or len(times) < 2 or any(input_sizes <= 0) or any(times <= 0):
        return "Not enough neither # items nor positive runtimes"
    # Define inline methods for common Big-O time complexities
    models = {
        "O(1) - Constant": lambda n, k=None: np.ones_like(n),
        "O(log n) - Logarithmic": lambda n, k=None: np.log2(n),
        "O(n) - Linear": lambda n, k=None: n,
        "O(n log n) - Quasi-Linear": lambda n, k=None: n * np.log2(n),
        "O(n log k) - Harmonic Quasi-Linear": lambda n, k: (n * np.log2(n)) / k if k else np.zeros_like(n),
        "O(n^2) - Quadratic": lambda n, k=None: n ** 2,
        "O(2^n) - Exponential)": lambda n, k=None: 2 ** n,
        "O(n!) - Factorial": lambda n, k=None: factorial_iterative(n),
    }
    # Normalize input_sizes and runtimes for fitting
    input_sizes_normalized = input_sizes / np.max(input_sizes)
    times_normalized = times / np.max(times)
    # Compute error for each model
    errors = {}
    for label, model in models.items():
        try:
            # Handle models requiring \k\
            if "k" in label and k is not None:
                predicted_times = model(input_sizes_normalized, k)
            else:
                predicted_times = model(input_sizes_normalized)
            # Compute mean squared error between predicted and actual runtimes
            mse = np.mean((predicted_times - times_normalized) ** 2)
            errors[label] = mse
        except Exception as e:
            # Skip impossible to fit/analyze models
            errors[label] = float('inf')
    # Find the model with the smallest error
    best_fit = min(errors, key=errors.get)
    return best_fit

def main():
    print(fizzBuzz(101))
    print("is 'level' palindrome? " + str(palindrome("level")))
    print("is 'rose' palindrome? " + str(palindrome("rose")))
    print("are 'listen' and 'silent' anagrams? " + str(is_anagram("listen", "silent")))
    print("are 'יהוה' and 'היוה' anagrams? " + str(is_anagram("יהוה", "היוה")))

    n_arr = [10,22,56,43,67,6,777,777**9]
    times = []
    input_szs = []
    for i in range(0, 10):
        start_time = time.time()
        print(f"Bubble Sort({str(n_arr)}) = {str(bubble_sort(n_arr))}")
        end_time = time.time()
        runtime = end_time - start_time
        input_szs.append(len(n_arr))
        times.append(runtime)
    print(f"Big-O Time Complexity ({max(times)} seconds): {estimate_big_o(input_szs, times)}")
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

    nums = [1,40,0,100,10,18**100,2,3,4,5,66,677,7,8**9,factorial_iterative(7)]
    print(f"Two numbers that add up 42 inside the following array {str(nums)} natural integers: {str(two_sum(nums, 42))}")

    my_heap = MinHeap()
    for n in nums:
        my_heap.push(n)

    while not my_heap.is_empty():
        n = my_heap.pop()
        print(f"My Heap: {str(n)}")

    json_data = '''{
  "name": "Alice",
  "age": 30,
  "isRemoteWorker": true,
  "skills": ["Python", "JavaScript", "Remote Collaboration"],
  "preferences": {
    "workHours": "flexible",
    "communication": "async",
    "tools": ["Slack", "Zoom", "Trello"]
  }
}
'''

    """
    print(f"Writing into workers.csv the new employee from JSON record: {json_data}")
    json_to_csv(json_data, 'workers.csv')

    with open('workers.csv', mode='r') as csv_file:
        rdr = csv.DictReader(csv_file)
        for row in rdr:
            print(row)
    """

    input_sz = []
    runtimes = []
    for i in range(0, 10):
        start_time = time.time()
        print(f"Harmony_Sort(Len: {len(nums)}) = {harmony_sort(nums, 10, 4)}")
        end_time = time.time()
        runtime = end_time - start_time
        input_sz.append(len(nums))
        runtimes.append(runtime)
    print(f"Big-O Time Complexity ({max(runtimes)} seconds): {estimate_big_o(input_sz, runtimes)}")


if __name__ == "__main__":
    main()